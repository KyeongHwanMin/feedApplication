# feedApplication


<img src="https://github.com/KyeongHwanMin/feedApplication/blob/main/feedApplication.png" width="400" height="400">

# 통합 소셜 미디어 피드 서비스
본 서비스는 유저 계정의 해시태그("#") 를 기반으로 `인스타그램`, `스레드`, `페이스북`, `트위터` 등 복수의 SNS에 게시된 게시물 중 유저의 해시태그가 포함된 게시물들을 하나의 서비스에서 확인할 수 있는 통합 Feed 어플리케이션 입니다.
이를 통해 본 서비스의 고객은 하나의 채널로 유저, 또는 브랜드의 SNS 노출 게시물 및 통계를 확인할 수 있습니다. 또한, 사용자는 게시물의 조회수, 좋아요 수, 공유 수 등의 통계를 확인할 수 있습니다.

<br/>

## Table of Contents
- [개요](#개요)
- [Skils](#skils)
- [Installation](#Installation)
- [API Reference](#api-reference)

<br/>


## 개요
현대의 소셜 미디어 사용자들은 페이스북, 인스타그램, 트위터와 같은 여러 플랫폼을 사용합니다. 
각 플랫폼별로 로그인하고 게시물을 확인하는 것은 시간이 많이 소요되며 비효율적입니다. 
특히, 특정 해시태그나 주제와 관련된 컨텐츠를 여러 플랫폼에서 일일이 찾아보는 것은 사용자에게 많은 노력이 들기 때문에 만들게 됨.



## Skils
가상환경: ![Static Badge](https://img.shields.io/badge/Venv-green)<br/>
언어 및 프레임워크: ![Static Badge](https://img.shields.io/badge/Python-3.12-blue) ![Static Badge](https://img.shields.io/badge/Django-REST-red)<br/>
<!-- 데이터 베이스: ![Static Badge](https://img.shields.io/badge/SQLite-blue) <br/>
배포 : ![Static Badge](https://img.shields.io/badge/Docker-039BC6) ![Static Badge](https://img.shields.io/badge/AWS-EC2-orange) ![Static Badge](https://img.shields.io/badge/Github-Actions-black)  <br/> ETC : ![Static Badge](https://img.shields.io/badge/Celery-black) ![Static Badge](https://img.shields.io/badge/Redis-red) -->

<br/>


## Installation


```bash
  # python 설치
  pyenv install 3.12.x
  # 가상환경 설치
  python -m venv venv
  # 가상환경 활성화
  venv/Scripts/activate
  # 의존성 설치
  pip install -r requirements.txt
  # 데이터베이스 마이그레이션
  python manage.py migrate
```

## 서버 정상 실행 확인
```bash
python manage.py runserver
```
위 명령 실행 결과로 아래와 같은 콘솔 출력이 뜨고, http://127.0.0.1:8000/ 접속이 되면 정상이다.
```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 10, 2023 - 13:40:31
Django version 4.0.10, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```


<!-- ## Running Tests

To run tests, run the following command

```bash
  npm run test
```

> Coverage ScreenShot ![Static Badge](https://img.shields.io/badge/Test_Passed-20/20-green)
![coverage](https://user-images.githubusercontent.com/48683566/56673924-0b84ae00-66b1-11e9-93ac-fb76ff96a5a0.png) -->



## API Reference


#### 회원가입 요청
```javascript
  POST api/v1/user/
```

| Parameter  | Type     | Description          |
|:-----------| :------- |:---------------------|
| `username` | `string` | **유저 ID**            |
| `email`  | `string` | **이메일**              |
| `password`  | `string` | **비밀번호** |

#### Response
```http
    HTTP/1.1 201
    Content-Type: application/json

    [{
        "username": "username",
        "email": "user@email.com",
        "verification_code": "6자리 숫자"
    },...
    ]
```


#### 회원가입 승인

#### Request
```javascript
  POST /api/v1/user/verification
```

| Parameter | Type     | Description         |
| :-------- | :------- |:--------------------|
| `username` | `string` | **유저  ID**          |
| `password` | `string` | **비밀번호**            |
| `verification_code` | `string` | **인증번호**            |

#### Response
```http
    HTTP/1.1 200
    Content-Type: application/json

    [{
        "회원가입이 승인되었습니다."
    },...
    ]
```


#### 로그인

#### Request
```javascript
  POST /api/v1/user/token
```

| Parameter | Type     | Description             |
| :-------- | :------- |:------------------------|
| `username` | `string` | **유저 ID** |
| `password` | `string` | **비밀번호** |

#### Response
```http
    HTTP/1.1 200
    Content-Type: application/json

    [{
    "refresh": "JWT TOKEN",
    "access": "JWT TOKEN"
    },...
    ]
```

#### 게시물 목록 보기

#### Request
```javascript
  GET api/v1/post/
```

#### Response
```http
    HTTP/1.1 200
    Content-Type: application/json

    [{
    "count": 13,
    "next": "http://127.0.0.1:8000/api/v1/post/?page=2",
    "previous": null,
    "results": [
        {
            "id": "cc47761d-c1cb-4fea-849d-4cc5272e895b",
            "hashtags": [
                "맛집",
                "맛없는집"
            ],
            "content_id": "1",
            "type": "instagram",
            "title": "인스타감성",
            "content": "인스타 감성의 글을 작성 해보았습니다.",
            "view_count": 5,
            "like_count": 2,
            "share_count": 4,
            "updated_at": "2023-10-29T12:59:38.506028Z",
            "created_at": "2023-10-29T12:35:54.849576Z",
            "user": 1
        },
        {
            "id": "7672bfee-0a0f-4485-9c98-23f6bd7b2a65",
            "hashtags": [
                "맛집",
                "맛없는집"
            ],
            "content_id": "",
            "type": "instagram",
            "title": "인스타감성",
            "content": "인스타 감성의 글을 작성 해보았습니다.",
            "view_count": 0,
            "like_count": 0,
            "share_count": 0,
            "updated_at": "2023-10-30T16:13:20.168950Z",
            "created_at": "2023-10-30T16:13:20.168950Z",
            "user": 1
        },...
    ]
```
#### 게시물 상세 보기

#### Request
```javascript
  GET api/v1/post/<str:pk>
```

#### Response
```http
    HTTP/1.1 200
    Content-Type: application/json

    [{
        "id": "7672bfee-0a0f-4485-9c98-23f6bd7b2a65",
        "hashtags": [
            "맛집",
            "맛없는집"
        ],
        "content_id": "",
        "type": "instagram",
        "title": "인스타감성",
        "content": "인스타 감성의 글을 작성 해보았습니다.",
        "view_count": 1,
        "like_count": 0,
        "share_count": 0,
        "updated_at": "2023-11-20T11:55:42.033254Z",
        "created_at": "2023-10-30T16:13:20.168950Z",
        "user": 1
        },...
    ]
```

#### 게시물 해시태그로 조회하기

#### Request
```javascript
  GET api/v1/post?hashtag=맛집
```

#### Response
```http
    HTTP/1.1 200
    Content-Type: application/json

    [{
        "count": 13,
        "next": "http://127.0.0.1:8000/api/v1/post/?hashtag=%EB%A7%9B%EC%A7%91&page=2",
        "previous": null,
        "results": [
            {
                "id": "cc47761d-c1cb-4fea-849d-4cc5272e895b",
                "hashtags": [
                    "맛집",
                    "맛없는집"
                ],
                "content_id": "1",
                "type": "instagram",
                "title": "인스타감성",
                "content": "인스타 감성의 글을 작성 해보았습니다.",
                "view_count": 5,
                "like_count": 2,
                "share_count": 4,
                "updated_at": "2023-10-29T12:59:38.506028Z",
                "created_at": "2023-10-29T12:35:54.849576Z",
                "user": 1
            },
            {
                "id": "7672bfee-0a0f-4485-9c98-23f6bd7b2a65",
                "hashtags": [
                    "맛집",
                    "맛없는집"
                ],
                "content_id": "",
                "type": "instagram",
                "title": "인스타감성",
                "content": "인스타 감성의 글을 작성 해보았습니다.",
                "view_count": 1,
                "like_count": 0,
                "share_count": 0,
                "updated_at": "2023-11-20T11:55:42.033254Z",
                "created_at": "2023-10-30T16:13:20.168950Z",
                "user": 1
            },
            {
                "id": "78b536c8-e01d-4502-88db-e1ca5095e760",
                "hashtags": [
                    "맛집",
                    "맛없는집"
                ],
                "content_id": "",
                "type": "instagram",
                "title": "인스타감성",
                "content": "인스타 감성의 글을 작성 해보았습니다.",
                "view_count": 0,
                "like_count": 0,
                "share_count": 0,
                "updated_at": "2023-10-30T16:13:21.392949Z",
                "created_at": "2023-10-30T16:13:21.392949Z",
                "user": 1
            }
        },...
    ]
```

#### 게시물 type 으로 조회하기

#### Request
```javascript
  GET api/v1/post?type=instagram
```

#### Response
```http
    HTTP/1.1 200
    Content-Type: application/json

    ["count": 13,
    "next": "http://127.0.0.1:8000/api/v1/post/?page=2&type=instagram",
    "previous": null,
    "results": [
        {
            "id": "cc47761d-c1cb-4fea-849d-4cc5272e895b",
            "hashtags": [
                "맛집",
                "맛없는집"
            ],
            "content_id": "1",
            "type": "instagram",
            "title": "인스타감성",
            "content": "인스타 감성의 글을 작성 해보았습니다.",
            "view_count": 5,
            "like_count": 2,
            "share_count": 4,
            "updated_at": "2023-10-29T12:59:38.506028Z",
            "created_at": "2023-10-29T12:35:54.849576Z",
            "user": 1
        },
        {
            "id": "7672bfee-0a0f-4485-9c98-23f6bd7b2a65",
            "hashtags": [
                "맛집",
                "맛없는집"
            ],
            "content_id": "",
            "type": "instagram",
            "title": "인스타감성",
            "content": "인스타 감성의 글을 작성 해보았습니다.",
            "view_count": 1,
            "like_count": 0,
            "share_count": 0,
            "updated_at": "2023-11-20T11:55:42.033254Z",
            "created_at": "2023-10-30T16:13:20.168950Z",
            "user": 1
        },...
    ]
```

#### 게시물 좋아요

#### Request
```javascript
  POST api/v1/post/likes/<str:content_id>
```

#### Response
```http
    HTTP/1.1 200
    Content-Type: application/json
    []
```
#### 날짜별 게시물 개수 조회

#### Request
```javascript
  GET api/v1/analytics?type=date&start=2023-11-15
```

#### Response
```http
    HTTP/1.1 200
    Content-Type: application/json
    [{
    "2023-11-15": 0,
    "2023-11-16": 0,
    "2023-11-17": 0,
    "2023-11-18": 0,
    "2023-11-19": 0,
    "2023-11-20": 1
    }]
```

#### 시간별 게시물 개수 조회

#### Request
```javascript
  GET api/v1/analytics?type=hour&start=2023-11-20 12:00
```

#### Response
```http
    HTTP/1.1 200
    Content-Type: application/json
    [{
    "2023-11-20 12:00": "count: 1",
    "2023-11-20 13:00": "count: 0",
    "2023-11-20 14:00": "count: 0",
    "2023-11-20 15:00": "count: 0",
    "2023-11-20 16:00": "count: 0",
    "2023-11-20 17:00": "count: 0",
    "2023-11-20 18:00": "count: 0",
    "2023-11-20 19:00": "count: 0",
    "2023-11-20 20:00": "count: 0",
    "2023-11-20 21:00": "count: 0"
    }]
```




<br/>
<<<<<<< HEAD








=======
>>>>>>> af8e8d11d793d5faa33fbabd2ca67fc5b5dfac5d
