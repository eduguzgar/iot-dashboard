# iot-dashboard
Fully integrated architecture platform with a dashboard for **Logistics Monitoring, _Internet of Things_**.

- Written in **Python**.
- **Flask** application as back-end.
- **PostgreSQL** as SQL database.
- Database connection pooling.
- Simple **dashboard** in plain HTML/CSS.
- **Communication protocol interface** for IoT devices.
- Communication protocol for the _Mictrack MT821/MT825_ GPS tracker in UDP multithreaded mode.
- **Geofences** to save GPS tracker battery when it is not in zone.
- Geofence alerts.

## Platform architecture

<img src="https://github.com/eduguzgar/iot-dashboard/blob/master/img/platform_architecture.png?raw=true" width="680">


## Dashboard layout

<img src="https://github.com/eduguzgar/iot-dashboard/blob/master/img/dashboard.png?raw=true" width="763" />

<img src="https://github.com/eduguzgar/iot-dashboard/blob/master/img/map_1.png?raw=true" width="380" /> <img src="https://github.com/eduguzgar/iot-dashboard/blob/master/img/map_2.png?raw=true" width="380" />
<img src="https://github.com/eduguzgar/iot-dashboard/blob/master/img/map_3.png?raw=true" width="380" /> <img src="https://github.com/eduguzgar/iot-dashboard/blob/master/img/map_4.png?raw=true" width="380" />


## Database schema

<img src="https://github.com/eduguzgar/iot-dashboard/blob/master/img/database_schema.png?raw=true" width="680">


## Pre-requisites 📋

- **Linux** operating system.
- **Python** (version >= 3.8) installed.
- **pip** installed.
- **PosgreSQL** server installed, I recommend lastest stable version. You can follow [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04). I also recommend to set up the configration file _"pg_hba.conf"_ and set a IPv4 host entry to listen at "0.0.0.0" address and allow md5 authentication, there are many guides about _"pg_hba.conf"_ out there.
- **Port forwarding** for the ports described [here](https://github.com/eduguzgar/iot-dashboard/blob/master/port_forwarding.txt).
- **pgAdmin 4** (Optional).


## Installation 🔧

Once you have met all the requirements mentioned in the previous section, just follow these steps:

- Clone or download this repo via HTTPS/SSH in your file system.
- Navigate to the repository directory:
```
cd /path/to/your/directory/iot-dashboard
```
- Create a new virtual environment in the root folder of the repository and activate it:
```
python3 -m venv venv
. venv/bin/activate
```
- Once the **virtual environment is activated** (you are inside it), install all required _Python_ packages from requirements:
```
pip install -r requirements.txt
```
- Finally, run the application installation script (if asked, enter your user password):
```
./scripts/install.sh
```


## Upgrade ⤵️

To upgrade all python packages simply run the upgrade script **within the virtual environment**:
```
./scripts/upgrade.sh
```


## Usage 🚀

### Start application

In order start **the entire application** just run the start script **within the virtual environment** (log files will be automatically created):
```
./scripts/start.sh
```
If you only wish to run the _Flask_ instance separately:
```
flask run --host=0.0.0.0
```
Finally, if you only wish to run the _Micktrack MT821/MT825_ communication protocol separately:
```
python -m comm_protocol.mt82x
```

### Shutdown application
```
./scripts/shutdown.sh
```

### Restart application
```
./scripts/restart.sh
```

### Application status
```
./scripts/status.sh
```
Be care the application **could have been started without this scripts** (e.g. starting manually from another folder), so the status and shutdown scripts could fail or show wrong results.