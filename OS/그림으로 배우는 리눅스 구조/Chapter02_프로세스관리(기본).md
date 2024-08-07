## 프로세스 생성

### 프로세스 확인

```bash
# 모든 프로세스 확인
ps aux
```

해당 명령어를 실행하면 PID, %CPU, %MEM 등 프로세스에 관한 정보를 얻을 수 있다. 

단순하게 프로세스의 개수를 알고 싶다면?

```bash
ps aux --no-header | wc -l
```

### 프로세스 생성

새로운 프로세스를 생성하는 목적은 다음 두 가지 경우이다.

- 동일한 프로그램 처리를 여러 프로세스에 나눠서 처리(웹서버에서 다수의 요청 받기)
- 다른 프로그램 생성(bash에서 각종 프로그램 새로 생성)

*첫 번째 경우는 저번 학기에 배운 [운영체제 과제](https://github.com/Kyeong6/operating-system/blob/main/assignment01/README.md)에서 수행하였다.  멀티 프로세스를 구현해서 요청에 대해 일대일 대응을 시키는 과제였다.* 

프로세스 생성을 실제로 실행하는 방법은 fork(), execve() 함수를 사용하는 것이다.

해당 함수는 내부적으로 각각 clone(), execve() 시스템콜을 호출한다. (저번 글에서의 이해가 필요하다. 함수 → 시스템 콜 → 커널)

첫 번째 경우는 fork()만, 두 번째 경우는 fork(), execve()를 모두 사용한다. 

**fork() 함수 : 자식 만들기**

fork() 함수는 간단하게 복사본을 만든다고 생각하면 된다. 원본이 부모(parent process), 복사본이 자식(child process)라고 부른다. 

- 실행 순서
    - 부모 프로세스가 fork() 함수 호출
    - 자식의 메모리 영역 확보한 후 부모 프로세스 메모리 복사
    - 부모와 자식 둘 다 fork() 함수에서 복귀(실행 끝 의미: 반환값 생성)
    - 부모와 자식은 반환값이 서로 달라서 분기 처리가 가능

*운영체제 과목에서 fork에 관하여 학습을 해서 다 알고있는 내용인 줄 알았는데 실행 순서(fork() 함수 복귀 …)에 관해서 이번 기회에 더 자세하게 배웠다. 다시 생각해보면 부모와 자식이 fork() 함수에서 복귀한다는 의미는 당연한 것이다. 역할이 끝났기 때문!*

*또한 프로세스 메모리를 복사하는 작업은 추후에 배울 내용이지만 카피 온 라이트 기능 덕분에 매우 적은 비용이라는 것이다. 그래서 **결과적으로 멀티 프로세스를 구현해도 오버헤드가 적지 않다는 것!***

**fork() 실습 진행**

```python
# fork.py

import os, sys

ret = os.fork()

if ret == 0:
	print("Child process pid={}, Parent process pid={}".format(os.getpid(), os.getppid())
	exit()
	
elif ret > 0:
	print("Parent process pid={}, Child process pid={}".format(os.getpid(), ret))
	exit()
	
sys.exit(1)
```

해당 스크립트를 생성하고 python3 ./fork.py를  수행하면 다음과 같은 결과를 얻는다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/0c79766f-e6e5-47fb-bb1f-6711656123dd/bdfd677f-0a1e-4e38-83e0-b59fdf1f87ea/Untitled.png)

정리하자면 fork() 함수에서 복귀한 후 반환값에 조건이 달라진다.

- 부모 프로세스 : 자식 프로세스의 ID 반환(ret > 0 조건)
- 자식 프로세스 : 0을 반환(ret == 0 조건)
  
<br/></br>
**execve() 함수 : 다른 프로그램을 기동**

fork() 함수로 프로세스 복사본을 만들었으면 자식 프로세스에서 execve() 함수를 호출하여 새로운 프로그램으로 바꾼다.

- 실행 순서
    - execve() 함수 호출
    - execve() 함수 인수로 지정한 실행 파일에서 프로그램을 읽어서 메모리에 배치하는데 필요한 정보 가져옴
    - 현재 프로세스의 메모리를 새로운 프로세스 데이터로 덮어씀
    - 프로세스를 새로운 프로세스의 최초에 실행할 명령(entry point)부터 실행 시작

(현재 프로세스 메모리 → execve() 실행 → 실행 파일의 새로운 프로세스 메모리 → 시작)

*fork() 함수를 호출한 후에 자식 프로세스는 execve() 함수에 의해서 인수로 지정한 프로세스로 변경된다는 의미! 이 구조를 fork-exec 구조라 한다.*

**execve() 실습 진행**

```python
# fork-and-exec.py

import os, sys

ret = os.fork()

if ret == 0:
	print("Child process pid={}, Parent process pid={}".format(os.getpid(), os.getppid())
	os.execve("/bin/echo", ["echo", "pid={} hi"].format(os.getpid())], {})
	exit()
	
elif ret > 0:
	print("Parent process pid={}, Child process pid={}".format(os.getpid(), ret))
	exit()
	
sys.exit(1)
```

해당 스크립트를 생성하고 python3 ./fork-and-exec.py를  수행하면 다음과 같은 결과를 얻는다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/0c79766f-e6e5-47fb-bb1f-6711656123dd/3e555612-208c-49e0-bc2d-87dfde905396/Untitled.png)

execve() 명령어로 인해서 hi가 나온 것을 알 수 있다. 결국 자식 프로세스 메모리에 echo 메모리가 바뀐 것이다.