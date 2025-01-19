up:
	docker-compose up --build -d
	@echo "Сервіс доступний за адресою: http://localhost:8000"

down:
	docker compose down
