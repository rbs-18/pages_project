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

- PostgreSQL

## HOW TO START PROJECT
- Clone repository and going:
```
git clone git@github.com:rbs-18/pages_project.git
cd /pages_project
```
- Create .env file (like template)

DEBUG=...

SECRET_KEY=...

ALLOWED_HOSTS=...

CELERY_BROKER_URL=...

CELERY_RESULT_BACKEND=...

DB_ENGINE=...

POSTGRES_USER=...

POSTGRES_PASSWORD=...

POSTGRES_DB=...

DB_HOST=...

DB_PORT=...

- Deploy and launch app:
```bash
docker-compose up -d --build
```

- Make migrations:
```bash
docker-compose exec web python manage.py migrate
```

- Fill database by data (optionally):
```bash
docker-compose exec web python manage.py loaddata fixtures.json
```

- Create superuser
```bash
docker-compose exec web python manage.py createsuperuser
```

*Infrastructure*
- web:
  port: 1337
- celery flower:
  port: 5555

# AUTHORS
*_Kozhevnikov Aleksei_*
