# RMSoft 채용 과제

## 1. 사용한 언어 및 프레임워크

- API 구현
  - Python Django v4.0.3
  - sqlite3 v3.33.0

- 테스트 환경
  - CentOS Stream release 9
  - docker v20.10.22
  - docker-compose v2.6.0



## 2. Docker hub
> https://hub.docker.com/repository/docker/wonwooo/rmsoft



## 3. 프로젝트 실행

* 환경 구축

  a. 도커 설치

  1. 도커 패키지 리포지토리 연결
    ```
    yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
    ```

  2. 패키지 설치
    ```
    yum -y install docker-ce
    ```

  3. 도커 서비스 시작
    ```
    systemctl start docker.service
    systemctl enable docker.service
    ```

  b. 도커 컴포즈 설치
  
  1. 도커 컴포즈 다운로드
    ```
    curl -L "https://github.com/docker/compose/releases/download/v2.6.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    ```

  2. 실행 권한 설정
    ```
    chmod +x /usr/local/bin/docker-compose
    ```

  c. 프로젝트 실행
  
  1. docker hub에서 이미지 다운로드
    ```
    docker pull wonwooo/rmsoft:latest
    ```

  2. docker-compose 파일 있는 경우, 해당 위치에서
    ```
    docker-compose up
    ```
        - background에서 daemon으로 실행하고 싶은 경우 -d 옵션
        - background에서 실행되는 경우 로그가 보고 싶으면 docker-compose logs -f

  3. docker-compose 파일이 없는 경우, git clone 후 해당 위치에서 실행
    ```
    git clone https://github.com/wonwooooo/rm_work.git
    cd rm_work
    docker-compose up
    ```



## 4. ERD
![image](https://user-images.githubusercontent.com/74032009/210040972-506af754-c1f9-44d3-bea5-ba0d4599aaaa.png)
