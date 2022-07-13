# pages_project

## DESCRIPTION
API service for monitoring pages. Admin can create new pages, new content (video, audio, text),
fill pages by content. Users can see pages and page content with API interface.

### POSTS
 - #### GETTING LIST OF Pages

 `api/v1/pages/` `GET`

```json
{
    "count": 0,
    "next": "http://example.com",
    "previous": "http://example.com",
    "results": [
        {
            "id": 0,
            "title": "string",
            "detail_information": "http://example.com",
            "contents": [
                {
                    "content_type": "string"
                }
            ]
        }
    ]
}
```
*Parameters*
pagination page

*Responses*

200

- #### GETTING CERTAIN GROUP

 `api/v1/pages/{page_id}/` `GET`

```json
{
    "id": 0,
    "title": "string",
    "contents": [
        {
            "content_type": "string",
            "content_object": "string"
        }
    ]
}
```

*Responses*

200, 404

## DOCUMENTATION AVAILIBLE AFTER LAUNCH:
http://127.0.0.1:8000/redoc/
http://127.0.0.1:8000/swagger/

## TECHNOLOGY

- Python 3.8
- Django 3.2
- Django Rest Framework 3.13
- Celery
- Docker

## DATABASE

- SQLite

## HOW TO START PROJECT
- Clone repository and going:
```
git clone git@github.com:rbs-18/pages_project.git -b with_sqllite
cd /pages_project
```

- Add .env (root) file and db.sqlite3 (page_app/)

- Deploy and launch app:
```bash
docker-compose up -d --build
```

web:
  port: 1337
celery flower:
  port: 5555

# AUTHORS
*Kozhevnikov Aleksei*
