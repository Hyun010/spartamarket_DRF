# spartamarket-DRF
### 프로젝트명 : 우리를 위한 중고거래(스파르타 마켓)
<p align="center">
  <br>
  <img src="./ref/supermarket.jpg" width=650 height=250>
  <br>
</p>
<br>

## 프로젝트 소개
### 우리가 아는 'ㄷㄱ' 홈페이지의 백엔드를 DRF를 사용하여 CRUD를 구현한 프로젝트
### 프로젝트 기간 : 2024.04.26 ~ 2024.05.02(7일)
<br>

## 기술 스택

| [Django](https://docs.djangoproject.com/ko/4.2/) | [Python](https://docs.python.org/ko/3.8/) |  [SQLite3](https://www.sqlite.org/docs.html)   
| :--------: | :--------: | :------: |
|   <img src="./ref/django.png" width=50 height=50>    |   <img src="./ref/python.png" width=50 height=30>    | <img src="./ref/SQLite3.png" width=60 height=45> 

## ERD
<p align="center">
  <br>
  <img src="./ref/ERD.png" width=650 height=250>
  <br>
</p>
<br>

## 구현 기능
### ACCOUNT
- 회원가입
<br><br>
<img src="./ref/회원가입_username_email.PNG" width=300 height=600>
<img src="./ref/회원가입_OK.PNG" width=300 height=600>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;username, email이 이미 존재한 경우&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 성공한 경우
<br><br>
- 로그인
<br><br>
<img src="./ref/로그인_username.PNG" width=300 height=600>
<img src="./ref/로그인_비밀번호.PNG" width=300 height=600>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;usernaem 없는 경우&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 비밀번호 없는 경우
<br><br>
<img src="./ref/로그인_OK.PNG" width=300 height=600>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;성공한 경우
<br><br>
- 프로필 조회
<br><br>
<img src="./ref/프로필조회_다른사람.PNG" width=300 height=600>
<img src="./ref/프로필조회_본인.PNG" width=300 height=600>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;다른 사람이 접근한 경우&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;본인이 접근한 경우
<br>

### PRODUCT
- 상품등록
<br><br>
<img src="./ref/상품등록_OK.PNG" width=300 height=600>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;다른 사람이 접근한 경우
<br><br>
- 상품조회
<br><br>
<img src="./ref/상품조회_OK_PAGINATION.PNG" width=300 height=600>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;물품 5개씩 페이지네이션
<br><br>
- 상품수정
<br><br>
<img src="./ref/상품수정_다른사람.PNG" width=300 height=600>
<img src="./ref/상품수정_본인_OK.PNG" width=300 height=600>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;다른사람 접근한 경우&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;본인 접근한 경우
<br><br>
- 상품삭제
<br><br>
<img src="./ref/상품삭제_다른사람.PNG" width=300 height=600>
<img src="./ref/상품삭제_본인.PNG" width=300 height=600>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;다른사람 접근한 경우&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;본인 접근한 경우


<br>

## API
<img src="./ref/accountsAPI.png" width=900 height=250>
<img src="./ref/productsAPI.png" width=900 height=250>
<br>

## PIP LIST
- requirements.txt 파일을 참고