# Rishabh Romit's Parity Backend (Django) !

Hi! This is my submission for the *Parity Backend (Django) Assignment*.

I've cloned the repo from [https://github.com/ParityInc/backend-assignment](https://github.com/ParityInc/backend-assignment) and added the commit titled 'start' as per the requirements.

# Usage
 1. Run the `sh one_time_setup.sh` bash script in a terminal (may take a few seconds depending on internet speed).
	 - This script downloads all dependencies (including PostgreSQL), sets up the Django application, performs DB migrations, creates super user and starts the local server.
 2. At the end of the script, once successful, it will start the local (Django) web server like this ):
 ```
 Running localserver at http://127.0.0.1:8008...

Performing system checks...

System check identified no issues (0 silenced).
January 22, 2020 - 04:39:43
Django version 2.1.15, using settings 'project.settings'
Starting development server at http://127.0.0.1:8008/
Quit the server with CONTROL-C.
 ```
 3. **NOTE:** Use `sh run.sh` for *subsequent* runs after using the `one_time_setup.sh`  to setup everything *initially*.

# API
In this section we explain the APIs supported by this application and their usage.
**NOTE:** All APIs require authentication (use the super user created above via Django admin panel).

## Houses
`HTTP Request URL` : [http://localhost:8008/houses/](http://localhost:8008/houses/)
`HTTP Methods Supported` : `GET, POST, HEAD, OPTIONS`
`HTTP GET Response` :
```
{
	"count": 1,
	"next": null,
	"previous": null,
	"results": [{
		"url": "http://localhost:8008/houses/51505739-4e8c-4fbb-855b-f1eff5c9f2b1/?format=json",
		"thermostats": [{
			"url": "http://localhost:8008/thermostats/af51d804-519b-4048-b446-a421d281c763/?format=json",
			"name": "NestThermostat001",
			"created_at": "2020-01-22T04:27:15.149753Z",
			"updated_at": "2020-01-22T04:31:06.295810Z",
			"mode": "heat",
			"current_temperature": "10.00",
			"temperature_set_point": "25.00",
			"house": "http://localhost:8008/houses/51505739-4e8c-4fbb-855b-f1eff5c9f2b1/?format=json"
		}],
		"rooms": [{
			"url": "http://localhost:8008/rooms/03944870-51c9-46e7-9afe-1b0fd86be613/?format=json",
			"lights": [{
				"url": "http://localhost:8008/lights/26f58581-c255-4e5f-8fcf-68289dedac7f/?format=json",
				"name": "Floor Lamp",
				"created_at": "2020-01-22T04:28:11.660576Z",
				"updated_at": "2020-01-22T04:29:19.134203Z",
				"state": "on",
				"room": "http://localhost:8008/rooms/03944870-51c9-46e7-9afe-1b0fd86be613/?format=json"
			}],
			"name": "Living Room",
			"created_at": "2020-01-22T04:29:09.092832Z",
			"updated_at": "2020-01-22T04:29:09.092850Z",
			"current_temperature": "25.00",
			"house": "http://localhost:8008/houses/51505739-4e8c-4fbb-855b-f1eff5c9f2b1/?format=json"
		}, {
			"url": "http://localhost:8008/rooms/60be5bc3-65aa-4640-84f5-d931de82ba26/?format=json",
			"lights": [{
				"url": "http://localhost:8008/lights/ff0eb565-e94c-49e9-8479-c202972ce39e/?format=json",
				"name": "Table Lamp",
				"created_at": "2020-01-22T04:28:58.290191Z",
				"updated_at": "2020-01-22T04:28:58.290209Z",
				"state": "off",
				"room": "http://localhost:8008/rooms/60be5bc3-65aa-4640-84f5-d931de82ba26/?format=json"
			}],
			"name": "Bed Room",
			"created_at": "2020-01-22T04:27:43.811365Z",
			"updated_at": "2020-01-22T04:32:33.454951Z",
			"current_temperature": "24.00",
			"house": "http://localhost:8008/houses/51505739-4e8c-4fbb-855b-f1eff5c9f2b1/?format=json"
		}],
		"created_at": "2020-01-22T04:26:37.027225Z",
		"updated_at": "2020-01-22T04:26:37.027247Z",
		"name": "House001"
	}]
}
```
#### HTTP POST [http://localhost:8008/houses/](http://localhost:8008/houses/)
`Request Content` :
```
{
    "name": "House Two"
}
```
`Content-Type`: `application/json`

`Response Content` :
```
{
	"url": "http://localhost:8008/houses/31bb59a4-e04b-4565-b23b-ba6c9c58a787/",
	"thermostats": [],
	"rooms": [],
	"created_at": "2020-01-22T05:01:57.320945Z",
	"updated_at": "2020-01-22T05:01:57.320997Z",
	"name": "House Two"
}
```

## Houses < ID >
`HTTP Request URL` : [http://localhost:8008/houses/<house_id>](http://localhost:8008/houses/<house_id>)
`HTTP Methods Supported` : `GET, PUT, PATCH, DELETE, HEAD, OPTIONS`
`HTTP GET Response` :
```
{
	"url": "http://localhost:8008/houses/31bb59a4-e04b-4565-b23b-ba6c9c58a787/",
	"thermostats": [],
	"rooms": [],
	"created_at": "2020-01-22T05:01:57.320945Z",
	"updated_at": "2020-01-22T05:01:57.320997Z",
	"name": "House Three"
}
```
#### HTTP PUT [http://localhost:8008/houses/<house_id>](http://localhost:8008/houses/<house_id>)
`Request Content` :
```
{
    "name": "House Two_1"
}
```
`Content-Type`: `application/json`

`Response Content` :
```
{
	"url": "http://localhost:8008/houses/31bb59a4-e04b-4565-b23b-ba6c9c58a787/",
	"thermostats": [],
	"rooms": [],
	"created_at": "2020-01-22T05:01:57.320945Z",
	"updated_at": "2020-01-22T05:01:57.320997Z",
	"name": "House Two_1"
}
```
#### HTTP PATCH [http://localhost:8008/houses/<house_id>](http://localhost:8008/houses/<house_id>)
`Request Content` :
```
{
    "name": "House Two"
}
```
`Content-Type`: `application/json`

`Response Content` :
```
{
	"url": "http://localhost:8008/houses/31bb59a4-e04b-4565-b23b-ba6c9c58a787/",
	"thermostats": [],
	"rooms": [],
	"created_at": "2020-01-22T05:01:57.320945Z",
	"updated_at": "2020-01-22T05:01:57.320997Z",
	"name": "House Two"
}
```
#### HTTP DELETE [http://localhost:8008/houses/<house_id>](http://localhost:8008/houses/<house_id>)
`Request Content` : `None`
`Response Content` :`HTTP 204 No Content`

## Thermostats
`HTTP Request URL` : [http://localhost:8008/thermostats/](http://localhost:8008/thermostats/)
`HTTP Methods Supported` : `GET, POST, HEAD, OPTIONS`
`HTTP GET Response` :
```
{
	"count": 1,
	"next": null,
	"previous": null,
	"results": [{
		"url": "http://localhost:8008/thermostats/af51d804-519b-4048-b446-a421d281c763/",
		"name": "NestThermostat001",
		"created_at": "2020-01-22T04:27:15.149753Z",
		"updated_at": "2020-01-22T04:31:06.295810Z",
		"mode": "heat",
		"current_temperature": "10.00",
		"temperature_set_point": "25.00",
		"house": "http://localhost:8008/houses/51505739-4e8c-4fbb-855b-f1eff5c9f2b1/"
	}]
}
```
#### HTTP POST [http://localhost:8008/thermostats/](http://localhost:8008/thermostats/)
`Request Content` :
```
{
    "name": "Google Home",
    "mode": "off",
    "current_temperature": 20.00,
    "temperature_set_point": 28.00,
    "house": "http://localhost:8008/houses/42111903-9eee-48b0-ab82-4338a6025280/"
}
```
`Content-Type`: `application/json`

`Response Content` :
```
{
	"url": "http://localhost:8008/thermostats/ae42a3d7-2bd8-47d4-9b1f-d666daa0cddd/",
	"name": "Google Home",
	"created_at": "2020-01-22T05:12:40.507265Z",
	"updated_at": "2020-01-22T05:12:40.507287Z",
	"mode": "off",
	"current_temperature": "20.00",
	"temperature_set_point": "28.00",
	"house": "http://localhost:8008/houses/42111903-9eee-48b0-ab82-4338a6025280/"
}
```

## Thermostats < ID >
`HTTP Request URL` : [http://localhost:8008/thermostats/<thermostat_id>](http://localhost:8008/thermostats/<thermostat_id>)
`HTTP Methods Supported` : `GET, PUT, PATCH, DELETE, HEAD, OPTIONS`
`HTTP GET Response` :
```
    "url": "http://localhost:8008/thermostats/ae42a3d7-2bd8-47d4-9b1f-d666daa0cddd/",
    "name": "Google Home",
    "created_at": "2020-01-22T05:12:40.507265Z",
    "updated_at": "2020-01-22T05:12:40.507287Z",
    "mode": "off",
    "current_temperature": "20.00",
    "temperature_set_point": "28.00",
    "house": "http://localhost:8008/houses/42111903-9eee-48b0-ab82-4338a6025280/"
}
```
#### HTTP PUT [http://localhost:8008/thermostats/<thermostat_id>](http://localhost:8008/thermostat/<thermostat_id>)
`Request Content` :
```
{
    "url": "http://localhost:8008/thermostats/ae42a3d7-2bd8-47d4-9b1f-d666daa0cddd/",
    "name": "Google Home",
    "created_at": "2020-01-22T05:12:40.507265Z",
    "updated_at": "2020-01-22T05:12:40.507287Z",
    "mode": "auto",
    "current_temperature": "20.00",
    "temperature_set_point": "28.00",
    "house": "http://localhost:8008/houses/42111903-9eee-48b0-ab82-4338a6025280/"
}
```
`Content-Type`: `application/json`

`Response Content` :
```
{
	"url": "http://localhost:8008/thermostats/ae42a3d7-2bd8-47d4-9b1f-d666daa0cddd/",
	"name": "Google Home",
	"created_at": "2020-01-22T05:12:40.507265Z",
	"updated_at": "2020-01-22T05:16:13.501401Z",
	"mode": "auto",
	"current_temperature": "20.00",
	"temperature_set_point": "28.00",
	"house": "http://localhost:8008/houses/42111903-9eee-48b0-ab82-4338a6025280/"
}
```
#### HTTP PATCH [http://localhost:8008/thermostats/<thermostat_id>](http://localhost:8008/thermostats/<thermostat_id>)
`Request Content` :
```
{
    "current_temperature": "25.00",
    "temperature_set_point": "29.00"
}
```
`Content-Type`: `application/json`

`Response Content` :
```
{
    "url": "http://localhost:8008/thermostats/ae42a3d7-2bd8-47d4-9b1f-d666daa0cddd/",
    "name": "Google Home",
    "created_at": "2020-01-22T05:12:40.507265Z",
    "updated_at": "2020-01-22T05:18:43.439288Z",
    "mode": "auto",
    "current_temperature": "25.00",
    "temperature_set_point": "29.00",
    "house": "http://localhost:8008/houses/42111903-9eee-48b0-ab82-4338a6025280/"
}
```
#### HTTP DELETE [http://localhost:8008/thermostats/<thermostat_id>](http://localhost:8008/thermostats/<thermostat_id>)
`Request Content` : `None`
`Response Content` :`HTTP 204 No Content`

## Rooms
`HTTP Request URL` : [http://localhost:8008/rooms/](http://localhost:8008/rooms/)
`HTTP Methods Supported` : `GET, POST, HEAD, OPTIONS`
`HTTP GET Response` :
```
{
	"count": 2,
	"next": null,
	"previous": null,
	"results": [{
			"url": "http://localhost:8008/rooms/60be5bc3-65aa-4640-84f5-d931de82ba26/",
			"lights": [{
				"url": "http://localhost:8008/lights/ff0eb565-e94c-49e9-8479-c202972ce39e/",
				"name": "Table Lamp",
				"created_at": "2020-01-22T04:28:58.290191Z",
				"updated_at": "2020-01-22T04:28:58.290209Z",
				"state": "off",
				"room": "http://localhost:8008/rooms/60be5bc3-65aa-4640-84f5-d931de82ba26/"
			}],
			"name": "Bed Room",
			"created_at": "2020-01-22T04:27:43.811365Z",
			"updated_at": "2020-01-22T04:32:33.454951Z",
			"current_temperature": "24.00",
			"house": "http://localhost:8008/houses/51505739-4e8c-4fbb-855b-f1eff5c9f2b1/"
		},
		{
			"url": "http://localhost:8008/rooms/03944870-51c9-46e7-9afe-1b0fd86be613/",
			"lights": [{
				"url": "http://localhost:8008/lights/26f58581-c255-4e5f-8fcf-68289dedac7f/",
				"name": "Floor Lamp",
				"created_at": "2020-01-22T04:28:11.660576Z",
				"updated_at": "2020-01-22T04:29:19.134203Z",
				"state": "on",
				"room": "http://localhost:8008/rooms/03944870-51c9-46e7-9afe-1b0fd86be613/"
			}],
			"name": "Living Room",
			"created_at": "2020-01-22T04:29:09.092832Z",
			"updated_at": "2020-01-22T04:29:09.092850Z",
			"current_temperature": "25.00",
			"house": "http://localhost:8008/houses/51505739-4e8c-4fbb-855b-f1eff5c9f2b1/"
		}
	]
}
```
#### HTTP POST [http://localhost:8008/rooms/](http://localhost:8008/rooms/)
`Request Content` :
```
{
    "name": "Kitchen",
    "current_temperature": 25.5,
    "house": "http://localhost:8008/houses/51505739-4e8c-4fbb-855b-f1eff5c9f2b1/"
}
```
`Content-Type`: `application/json`

`Response Content` :
```
{
	"url": "http://localhost:8008/rooms/b282e216-41bc-4530-9d09-e549df0b3d2d/",
	"lights": [],
	"name": "Kitchen",
	"created_at": "2020-01-22T05:23:29.505898Z",
	"updated_at": "2020-01-22T05:23:29.505919Z",
	"current_temperature": "25.50",
	"house": "http://localhost:8008/houses/51505739-4e8c-4fbb-855b-f1eff5c9f2b1/"
}
```

## Rooms < ID >
`HTTP Request URL` : [http://localhost:8008/rooms/<room_id>](http://localhost:8008/rooms/<room_id>)
`HTTP Methods Supported` : `GET, PUT, PATCH, DELETE, HEAD, OPTIONS`
`HTTP GET Response` :
```
{
	"url": "http://localhost:8008/rooms/b282e216-41bc-4530-9d09-e549df0b3d2d/",
	"lights": [],
	"name": "Kitchen",
	"created_at": "2020-01-22T05:23:29.505898Z",
	"updated_at": "2020-01-22T05:23:29.505919Z",
	"current_temperature": "25.50",
	"house": "http://localhost:8008/houses/51505739-4e8c-4fbb-855b-f1eff5c9f2b1/"
}
```
#### HTTP PUT [http://localhost:8008/rooms/<room_id>](http://localhost:8008/rooms/<room_id>)
`Request Content` :
```
{
    "url": "http://localhost:8008/rooms/03944870-51c9-46e7-9afe-1b0fd86be613/",
    "lights": [
        {
            "url": "http://localhost:8008/lights/26f58581-c255-4e5f-8fcf-68289dedac7f/",
            "name": "Floor Lamp",
            "created_at": "2020-01-22T04:28:11.660576Z",
            "updated_at": "2020-01-22T04:29:19.134203Z",
            "state": "on",
            "room": "http://localhost:8008/rooms/03944870-51c9-46e7-9afe-1b0fd86be613/"
        }
    ],
    "name": "Living Room",
    "created_at": "2020-01-22T04:29:09.092832Z",
    "updated_at": "2020-01-22T04:29:09.092850Z",
    "current_temperature": "28.00",
    "house": "http://localhost:8008/houses/51505739-4e8c-4fbb-855b-f1eff5c9f2b1/"
}
```
`Content-Type`: `application/json`

`Response Content` :
```
{
    "url": "http://localhost:8008/rooms/03944870-51c9-46e7-9afe-1b0fd86be613/",
    "lights": [
        {
            "url": "http://localhost:8008/lights/26f58581-c255-4e5f-8fcf-68289dedac7f/",
            "name": "Floor Lamp",
            "created_at": "2020-01-22T04:28:11.660576Z",
            "updated_at": "2020-01-22T04:29:19.134203Z",
            "state": "on",
            "room": "http://localhost:8008/rooms/03944870-51c9-46e7-9afe-1b0fd86be613/"
        }
    ],
    "name": "Living Room",
    "created_at": "2020-01-22T04:29:09.092832Z",
    "updated_at": "2020-01-22T05:25:43.846538Z",
    "current_temperature": "28.00",
    "house": "http://localhost:8008/houses/51505739-4e8c-4fbb-855b-f1eff5c9f2b1/"
}
```
#### HTTP PATCH [http://localhost:8008/rooms/<room_id>](http://localhost:8008/rooms/<room_id>)
`Request Content` :
```
{
    "current_temperature": "20.10"
}
```
`Content-Type`: `application/json`

`Response Content` :
```
{
	"url": "http://localhost:8008/rooms/b282e216-41bc-4530-9d09-e549df0b3d2d/",
	"lights": [],
	"name": "Kitchen",
	"created_at": "2020-01-22T05:23:29.505898Z",
	"updated_at": "2020-01-22T05:27:11.340594Z",
	"current_temperature": "20.10",
	"house": "http://localhost:8008/houses/51505739-4e8c-4fbb-855b-f1eff5c9f2b1/"
}
```
#### HTTP DELETE [http://localhost:8008/rooms/<room_id>](http://localhost:8008/rooms/<room_id>)
`Request Content` : `None`
`Response Content` :`HTTP 204 No Content`

## Lights
`HTTP Request URL` : [http://localhost:8008/lights/](http://localhost:8008/lights/)
`HTTP Methods Supported` : `GET, POST, HEAD, OPTIONS`
`HTTP GET Response` :
```
{
	"count": 2,
	"next": null,
	"previous": null,
	"results": [{
			"url": "http://localhost:8008/lights/ff0eb565-e94c-49e9-8479-c202972ce39e/",
			"name": "Table Lamp",
			"created_at": "2020-01-22T04:28:58.290191Z",
			"updated_at": "2020-01-22T04:28:58.290209Z",
			"state": "off",
			"room": "http://localhost:8008/rooms/60be5bc3-65aa-4640-84f5-d931de82ba26/"
		},
		{
			"url": "http://localhost:8008/lights/26f58581-c255-4e5f-8fcf-68289dedac7f/",
			"name": "Floor Lamp",
			"created_at": "2020-01-22T04:28:11.660576Z",
			"updated_at": "2020-01-22T04:29:19.134203Z",
			"state": "on",
			"room": "http://localhost:8008/rooms/03944870-51c9-46e7-9afe-1b0fd86be613/"
		}
	]
}
```
#### HTTP POST [http://localhost:8008/lights/](http://localhost:8008/lights/)
`Request Content` :
```
{
    "name": "Side Table Yellow Lamp",
    "state": "on",
    "room": "http://localhost:8008/rooms/03944870-51c9-46e7-9afe-1b0fd86be613/"
}
```
`Content-Type`: `application/json`

`Response Content` :
```
{
	"url": "http://localhost:8008/lights/4d6fc28d-b1d7-403a-9e34-cbc5384eff12/",
	"name": "Side Table Yellow Lamp",
	"created_at": "2020-01-22T05:30:47.386292Z",
	"updated_at": "2020-01-22T05:30:47.386320Z",
	"state": "on",
	"room": "http://localhost:8008/rooms/03944870-51c9-46e7-9afe-1b0fd86be613/"
}
```

## Rooms < ID >
`HTTP Request URL` : [http://localhost:8008/lights/<light_id>](http://localhost:8008/lights/<light_id>)
`HTTP Methods Supported` : `GET, PUT, PATCH, DELETE, HEAD, OPTIONS`
`HTTP GET Response` :
```
{
	"url": "http://localhost:8008/lights/4d6fc28d-b1d7-403a-9e34-cbc5384eff12/",
	"name": "Side Table Yellow Lamp",
	"created_at": "2020-01-22T05:30:47.386292Z",
	"updated_at": "2020-01-22T05:30:47.386320Z",
	"state": "on",
	"room": "http://localhost:8008/rooms/03944870-51c9-46e7-9afe-1b0fd86be613/"
}
```
#### HTTP PUT [http://localhost:8008/lights/<light_id>](http://localhost:8008/lights/<light_id>)
`Request Content` :
```
{
    "url": "http://localhost:8008/lights/4d6fc28d-b1d7-403a-9e34-cbc5384eff12/",
    "name": "Side Table Yellow Lamp",
    "created_at": "2020-01-22T05:30:47.386292Z",
    "updated_at": "2020-01-22T05:30:47.386320Z",
    "state": "off",
    "room": "http://localhost:8008/rooms/03944870-51c9-46e7-9afe-1b0fd86be613/"
}
```
`Content-Type`: `application/json`

`Response Content` :
```
{
	"url": "http://localhost:8008/lights/4d6fc28d-b1d7-403a-9e34-cbc5384eff12/",
	"name": "Side Table Yellow Lamp",
	"created_at": "2020-01-22T05:30:47.386292Z",
	"updated_at": "2020-01-22T05:31:25.829106Z",
	"state": "off",
	"room": "http://localhost:8008/rooms/03944870-51c9-46e7-9afe-1b0fd86be613/"
}
```
#### HTTP PATCH [http://localhost:8008/lights/<light_id>](http://localhost:8008/lights/<light_id>)
`Request Content` :
```
{
	"state": "on"
}
```
`Content-Type`: `application/json`

`Response Content` :
```
{
	"url": "http://localhost:8008/lights/4d6fc28d-b1d7-403a-9e34-cbc5384eff12/",
	"name": "Side Table Yellow Lamp",
	"created_at": "2020-01-22T05:30:47.386292Z",
	"updated_at": "2020-01-22T05:32:05.566125Z",
	"state": "on",
	"room": "http://localhost:8008/rooms/03944870-51c9-46e7-9afe-1b0fd86be613/"
}
```

#### HTTP DELETE [http://localhost:8008/lights/<light_id>](http://localhost:8008/lights/<light_id>)
`Request Content` : `None`
`Response Content` :`HTTP 204 No Content`

# State change Information:
As per the requirement:
>We would also like to track change of state of each light, thermostat, and room temperature (ie. when the thermostat changes from “off” to “cool” we need a record of the change occurring and when it occurred).

This has been implemented by creating the following schemas to track state changes of Thermostats, Rooms and Lights respectively:
1. LightStateChangeInformation
2. ThermostatStateChangeInformation
3. RoomStateChangeInformation

All the above schemas keep track of changes made to their respective "models" by overriding the **update** and
**partial_update** methods (part of *django-rest-framework's* *ModelViewSet*).

What we do here is store the *current_state* of an instance (say, a *thermostat* instance) and the *next_state* of the instance which it will be in *after* the update (HTTP PUT or PATCH).

These are JSON (PostgreSQL native JSON support) fields in the schema which hold the exact change that was made and not the entire object. This helps in keeping track without having resorting to finding needle in a haystack.

##### One such example is shown below, more in the screenshots.
`Schema:` `homes_thermostatchangeinformation`
| created_at | updated_at |id|previous_state|next_state|thermostat_id|
|--|--|--|--|--|--|
|2020-01-22 05:18:43.44683+00|2020-01-22 05:18:43.446853+00|129c54e3-0b8d-4933-b53f-f4da09217eb3|{"current_temperature": "20.00", "temperature_set_point": "28.00"}|{"current_temperature": "25.00", "temperature_set_point": "29.00"}|ae42a3d7-2bd8-47d4-9b1f-d666daa0cddd|


**NOTE:** Using the information stored in the state change scehmas - we can build specific endpoints to show (historical) state change data (which accepts a pair of date/datetimes in addition to resource IDs) to show/track changes over time.

# Troubleshooting
 1. If you see the message `This setup assumed Docker is installed on this machine.
  If not, see: https://docs.docker.com/v17.09/engine/installation/` this means docker application is not installed or running locally.
 2.  If you see the message  `This setup assumed Pipenv is installed on this machine.
  If not, see: https://github.com/pypa/pipenv` this means that the pipenv application is not available locally on the machine and needs to be installed either via `brew install pipenv` (macOS) or similar steps for other OS'es as mentioned in the pipenv github link.
  3. If you see the following message:
```
   django.db.utils.OperationalError: could not connect to server: No such file or directory 	
   Is the server running locally and accepting
   connections on Unix domain socket "/tmp/.s.PGSQL.5432"?
   ```
- then it either means that the PostgreSQL docker container (downloaded as part of the `one_time_setup.sh` script is not running
- or, the `POSTEGRES_*` environment variables have not been exported in the current shell.
4. **NOTE:** Use `sh run.sh` for subsequent runs after using the `one_time_setup.sh`  to setup everything initially.


# Contact
Maintainer Name: Rishabh Romit<br/>
Maintainer Email: rishabh.romit@gmail.com
