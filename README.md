# kakao_aws_rpa
- AWS 서비스를 사용해서 카카오톡으로 RPA 제어하기
- AWS 기반의 서비스(Lambda, S3, API Gateway 등)를 이용해 물리적인 환경(서버, 네트워크)에 제약이 없음
- 대부분의 스마트폰 유저가 사용하고 있는 카카오 톡을 이용해 손쉬운 RPA 접근 가능

- 환경 및 사용언어
1. Kakao Open Builder
2. AWS (Lambda, API Gateway, S3)
3. RPA (Windows Server 2012, MsSql, CA Certi)
4. Python 3.X, C#


![1](https://user-images.githubusercontent.com/85280844/147725776-f14e29ea-150d-4a51-ae63-d450bba8b556.PNG)
![2](https://user-images.githubusercontent.com/85280844/147725782-42891d30-c747-4914-8254-ee66e91fd213.PNG)
![3](https://user-images.githubusercontent.com/85280844/147725790-1138ca7d-686e-4856-a780-adc1edc94ce9.PNG)
![4](https://user-images.githubusercontent.com/85280844/147725795-d6f257b3-25d2-4fec-85dd-65050663c336.PNG)


#특이사항
- Token은 OAuth2.0 사용
- 각 Url은 post/get filter 걸어서 특정 작업만 수행 가능
- Releases key는 작업수행 시 필요 (고유한 값임)
- 작업실행시에 리턴되는 key로 작업 상태 파악 가능 (실행마다 매번 다름)


#
1. 사용자 인증
  - call : 아이디와 비밀번호
  - return  : O -> 인증 완료 메시지 전송
                X -> 실패 및 재시도 메시지 전송

2. 작업 실행
  - call : 특정 작업 실행
  - return : O -> 작업 실행 및 실행 완료 메시지 전송
               X -> 작업 실행 실패 메시지 전송

3. 작업 확인
  - call : 실행중인 작업 상태 확인
  - return  : 실행 작업 상태 메시지 전송

4. 작업 리스트
  - call : 실행 가능한 작업 리스트 확인
  - return : 작업 리스트 전송

5. 작업 별 수행 시간
  - call : 작업의 수행 시간 확인
  - return : 작업의 수행 시간 전송

6. 실행중인 작업의 예상 종료 시간
  - call : 실행중인 작업 예상 종료시간 확인
  - return : 실행중인 작업의 시작 시간과 평균 수행 시간을 비교해 예상 종료 시간 전송

