# Diary
일기장 같은 블로그 개인 프로젝트 입니다.

# 사용한 기술스택
- Python
- Django
- Djaong-allauth
- Mysql
- Bootstrap4

# 구현기능
* 계정관련
  - 로그인, 로그아웃, 회원가입
  - 비밀번호 찾기
  - 프로필 수정
  - 팔로우. 팔로

* 유효성 검사
  - 닉네임은 특수문자를 사용 할 수 없다.
  - 이메일은 중복이 불가능하다.
  - 비밀번호는 8자 이상의 영문 대/소문자, 숫자, 특수문자를 포함해야 한다.
* 중복확인
  - 닉네임 중복 시 "이미 사용중인 닉네임입니다."의 메시지를 보여주기
  - 이메일이 중복 시
* 로그인 검사
  - 아이디와 비밀번호가 일치하지 않을 시 "아이디 또는 비밀번호가 일치하지 않습니다. "의 메시지를 보여주기
  - 모든 검사가 통과하면 이메일 인증 페이지로 이동
* 이메일 인증
  - 기능 구현 중(지금은 콘솔로 보내는 중)
* 로그인을 하지 않은 경우 아래 페이지만 이용가능
  - 회원가입
  - 로그인
  - 게시글 목록 페이지
  - 게시글 상세보기 페이지
  - 게시글 작성자 프로필 페이지

* 게시판
    - 게시글 CRUD
    - 댓글 달기
    - 댓글 수정/삭제
    - 페이징
* 게시글 검사 
  - 게시글 수정 및 삭제는 해당 작성자만 가능
  - 점수는 0 ~ 10 사이 만 가능
  - feeling은 특수문자와 숫자는 들어 갈 수 없다.
  - 로그인을 하지않고 글쓰기를 누르면 로그인 페이지로 이동
* 댓글 검사
  - 로그인 하지않으면 로그인 페이지로 이동
  - 댓글 수정 및 삭제는 해당 작성자만 가능
  - 게시글 삭제 시 해당 댓글 데이터도 같이 삭제
* 프로필
  - 사진 수정 및 소개글
  - 팔로우/팔로
  - 팔로우/팔로윙 한 목록

# 이미지
## 게시글 관련
* 홈화면  
  - 게시판 목록 페이지로 이동  가능
  - 로그인, 회원가입 후 홈화면으로 이동
![홈](https://user-images.githubusercontent.com/67260228/185420212-360c7e4b-f35a-4900-b9d2-1b10915d628b.png)
* 게시판 목록 페이지  
  - 글쓰기 기능
  - 소개글, 프로필 이동 가능
  - 페이징
![게시판 목록](https://user-images.githubusercontent.com/67260228/185420419-f7314c43-2823-4a50-bf47-e2f7ed1a2bcb.png)

* 글쓰기 페이지 
  - 로그인한 사용자만 새로운글 작성 가능
  - 로그인 후 글쓰기 페이지로 이동
![image](https://user-images.githubusercontent.com/67260228/185420894-903781e6-7ff6-420b-85bf-f20ff9385210.png)
* 상세 페이지  
  - 본인이 작성한 글만 수정 및 삭제 가능
![image](https://user-images.githubusercontent.com/67260228/185421054-37109079-eb79-42ab-9e87-26a19aaea9c9.png)  
  - 게시글 수정  
![image](https://user-images.githubusercontent.com/67260228/185422525-1ab829c6-c5ad-424b-98b9-8dc385331e71.png)
  - 게시글 삭제  
![image](https://user-images.githubusercontent.com/67260228/185422765-2c490dcc-9852-4629-a9dd-cf910a054eee.png)

* 댓글  
  - 상세페이지의 댓글 입력가능
  - 댓글의 수 표시
  - 작성자 본인의 댓글만 수정 및 삭제 가능
![image](https://user-images.githubusercontent.com/67260228/185421223-8fcb10bc-6f1a-4fb2-b89c-c6e958bc3287.png)  
![image](https://user-images.githubusercontent.com/67260228/185421333-8759d0e4-e620-418d-8aed-f9d5b7f1b7dc.png)
  - 댓글 삭제  
![image](https://user-images.githubusercontent.com/67260228/185422852-b4e3d046-8a4e-422d-87fb-fe79b2e40970.png)
  - 댓글 수정  
![image](https://user-images.githubusercontent.com/67260228/185423020-874f613d-0d49-4809-88ef-43142722766b.png)
* 좋아요  
  - 게시글의 좋아요 기능
  - 좋아요 누르지 않을 때
![image](https://user-images.githubusercontent.com/67260228/185423155-3313726a-0f63-4807-a1ad-1e5ef34dada3.png)
  - 좋아요 눌렀을 때
![image](https://user-images.githubusercontent.com/67260228/185423217-6806e384-6457-4e80-a09c-a5bec2900c29.png)

* 회원가입  
  - 닉네임, 이메일 중복 검사
  - 비밀번호 유효성 검사
![image](https://user-images.githubusercontent.com/67260228/185420597-89ee495e-ef9a-4550-a00b-868c88ff5aa7.png)
* 로그인  
  - 
![image](https://user-images.githubusercontent.com/67260228/185420708-a284f20b-f30c-461d-8c05-1febda31e891.png)

## 프로필
* 프로필 페이지 
  - 프로필 수정 기능 
  - 팔로우 및 팔로잉 기능
  - 팔로우 및 팔로잉 목록 보기 기능
  - 프로필 주인의 최근 2개 작성글 표시
![image](https://user-images.githubusercontent.com/67260228/185429017-aa3f680b-fb3c-405f-888e-d9bf8b941a35.png)
  - 팔로우 목록  
![image](https://user-images.githubusercontent.com/67260228/185422139-02e9cf4c-11e0-43e0-8bfa-9c7bb384ccaa.png)
  - 팔로잉 목록  
![image](https://user-images.githubusercontent.com/67260228/185422265-0777e5f0-7e66-4ef7-a83a-3bfc338d0dd6.png)
* 프로필 주인의 작성글
  - 총 게시글 개수 표시
  - 페이징
![image](https://user-images.githubusercontent.com/67260228/185430984-70ca7e0f-d026-4b67-818c-338fd90616eb.png)

* 프로필 수정  
  - 자신의 프로필만 수정 가능
  - 이미지 및 소개글 작성 가능
![image](https://user-images.githubusercontent.com/67260228/185429841-695614b7-3839-4686-96ff-ec54f0244c9a.png)
![image](https://user-images.githubusercontent.com/67260228/185421605-9b43135e-4f74-4268-bb75-9c84fdd8df33.png)

# 추가기능
## 소셜 로그인
---
* 구글 로그인
  ![image](https://user-images.githubusercontent.com/67260228/194020268-fbb3adb9-de3b-42ce-83b6-52beafe78e2b.png)
## 대댓글
* 로그인 한 유저만 댓글 달기 가능
 ![image](https://user-images.githubusercontent.com/67260228/194020473-1d191b9a-7f7d-4fa1-98c7-fbaf4f445376.png)
