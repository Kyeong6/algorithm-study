대용량 트래픽 처리 시스템에서 분산 처리를 하고있는데, 이때 Kafka를 사용하고 있다.

### Kafka

- 데이터 스트림을 실시간으로 처리하고 저장하기 위해 고안
- 많은 양의 데이터를 효율적으로 처리하면서도 높은 처리량과 낮은 지연 시간을 제공
- 위의 장점을 활용하여 카프카는 대규모 데이터 파이프라인, 실시간 로그 데이터 수집 및 모니터링 시스템 등 다양한 용도로 사용

### Kafka 시스템의 3가지 구조

<img width="789" alt="1" src="https://github.com/user-attachments/assets/08746204-b050-451a-bed6-2e3046cc7794">

- Producer
- Kafka Cluster
    - 처리해야 할 데이터를 쌓아두고 있는 데이터 저장소
- Consumer

처리해야할 `이벤트` 를 Producer에게 넣어주면 Kafka Cluster가 보관하고 있다가 Consumer가 순차적으로 처리하게 되는 구조

**사전 지식**

- Topic:
    - Kafka는 이벤트를 `Topic` 이라는 개념으로 구성
    - 주제별로 관련된 이벤트를 모으는 단위(분류 단위)
    - Kafka Cluster는 처리해야할 데이터를 Topic 단위로 가지고 있음
    - Topic으로 이벤트가 구분되기 때문에 Producer와 Consumer는 하나의 Kafka Cluster 안에서 각자의 관심사를 분리할 수 있음
- Partition:
    - Topic은 한 개 이상의 Partition으로 구성
    - 새로운 이벤트가 Topic으로 들어오면 뒤에 어펜드 형식으로 추가되며, 오프셋을 할당받게 되어 오프셋이 메시지를 식별할 수 있는 유니크한 값이 됨
    - 오프셋을 기준으로 이벤트는 순차적으로 Consumer에 의해 처리

Kafka는 Topic 단위로 Partition을 지원하기 때문에 Consumer가 발생한 이벤트는 Partition이 여러 개일 경우 여러 개로 나뉘어서 저장하고, Consumer도 Partition별로 따로 붙을 수 있기 때문에 `병렬 분산처리`가 용이

### Producer

<img width="781" alt="2" src="https://github.com/user-attachments/assets/1d2b9275-8675-4798-9c1b-78d061d28da8">

- Producer는 데이터를 생성하고, Kafka Cluster로 전송하는 역할
    - 데이터 생성 후 Kafka Topic으로 데이터를 보내는 것

*Producer는 단어 그대로 처리해야 될 일을 생산하는 `생산자` 역할*

### Consumer

<img width="807" alt="3" src="https://github.com/user-attachments/assets/324ce8fa-2454-4649-835d-8d86a5126eae">

- Consumer는 Topic에서 데이터를 읽어오는 역할
    - 데이터를 소비하고 처리하는 것

*Consumer는 Kafka Cluster에서 읽어온 데이터를 어플리케이션의 로직에 따라 처리하거나 다른 시스템으로 전달하는 `전달자` 역할*

- 추가적으로 읽어온 데이터의 오프셋(위치)를 기록하여 자체적으로 읽은 데이터의 위치를 추적
    - Consumer가 중단된 지점부터 데이터를 다시 읽거나 특정 범위의 데이터만을 읽어올 수 있는 이유

### Kafka 운영과 유지보수 담당 : Broker

<img width="748" alt="4" src="https://github.com/user-attachments/assets/18f55faf-642c-4c83-82e0-2a336d58c181">

- Broker는 데이터의 저장과 전달을 관리하며 Producer로부터 전송된 데이터를 Topic에 저장하고, Consumer에게 필요한 데이터 제공
    - 실질적으로 데이터를 관리하는 역할을 담당하는 것이 `Broker`
- Kafka Cluster는 여러 개의 Broker로 구성되며 각 Broker는 데이터의 Partition을 관리하고 데이터의 복제 및 장애 조치 기능을 수행
- Broker는 데이터의 처리량과 안정성 확보를 위해서 확장 가능한 방식으로 설계

### Zookeeper

- Zookeeper는 Kafka Cluster의 구성 정보와 상태를 분산 형상관리 도구 
→ Kafka Cluster의 안정성 일관성 보장
    - Kafka Cluster 구성 및 변경
        - Broker의 추가 및 제거
        - Topic의 생성 및 삭제
    - Topic의 metadata
    - Broker의 상태
    - Consumer 그룹 추적 및 유지
    - Broker들 간의 리더 선출 및 동기화
    - 이벤트 처리 등 분산 시스템 작업 수행

### 그럼 왜 Kafka를 사용하는가?

- 데이터 영속성
    - RabbitMQ와 같은 시스템과 비교하였을 때 일반적인 Message Queue 시스템들의 메모리 상에서 동작하여 시스템이 꺼지면 모든 메시지들이 유실되는 문제 존재(In-Memory 특징)
    - 이와 반대로 Kafka는 디스크에 이벤트를 저장하기 때문에 문제가 생겨 시스템이 다운되더라도 복구가 가능
- 효과적인 대규모 트래픽 분산처리
    - Topic 내에 Partition을 설정함으로써 대규모의 트래픽을 병렬적으로 분산처리가 가능
    - Partition을 줄이는 것은 어렵지만, 늘리는 것은 쉽기 때문에 서비스가 빠르게 성장하는 경우 스케일업이 쉬움
- 안정성
    - 다른 분야의 분산 시스템들처럼 Cluster의 Failover, Replication이 가능
        - Failover : 컴퓨터 서버, 시스템 등에서 이상이 생겼을 때 예비 시스템 자동전환 기능
        - Replication : 데이터 저장과 백업하는 방법과 관련이 있는 데이터를 호스트 컴퓨터에서 다른 컴퓨터로 복사
    - Zookeeper가 Cluster의 관리를 해주기 때문에 안정적으로 운영 가능