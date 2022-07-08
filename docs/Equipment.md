# Оборудование

| # | Роут                       | Действие                                                                                                                 |
|---|----------------------------|--------------------------------------------------------------------------------------------------------------------------|
| 1 | GET:/api/equipment         | Вывод пагинированного списка оборудования с возможностью поиска путем указания query параметров советующим ключам ответа |
| 2 | GET:/api/equipment/{id}    | Запрос данных по id                                                                                                      |
| 3 | POST:/api/equipment        | Создание новой(ых) записи(ей)                                                                                            |
| 4 | PUT:/api/equipment/{id}    | Редактирование записи                                                                                                    |
| 5 | DELETE:/api/equipment/{id} | Удаление записи (мягкое удаление)                                                                                        |


# Получение списка
```json
{
	"count": 1,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 5,
			"equipment_type": {
				"id": 1,
				"name": "TP-Link DIR-300",
				"mask": "XXAAAAAXAA"
			},
			"serial_number": [
				"70BABCDE9M"
			],
			"description": null
		}
	]
}
```


# Создание записи

* Пример запроса:
```json
{
	"mask": "XXAAAAAXAA",
	"serial_number": ["70BABCDE9M"],
	"equipment_type_id": 1
}
```


# Редактирование
* Пример запроса:
```json
{
	"mask": "XXAAAAAXAA",
	"serial_number": ["70BABCDE9F"],
	"equipment_type_id": 2
}
```