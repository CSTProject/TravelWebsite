import requests

api_key = 'k8i2c5h19h'

class LiveTrain():
    def __init__(self,train_no,date):
        self.train_no = str(train_no)
        self.date = str(date)
        self.data = self.get_live_status()
    
    def get_live_status(self):
        req = requests.get('http://api.railwayapi.com/v2/live/train/{}/date/{}/apikey/{}/'.format(self.train_no,self.date,api_key))
        data = req.json()
        return data
    
    
    def routelist(self):
        return self.data['route']
    
    def no(self):
        return self.data['current_station']['no']
    
    def name_code(self):
        return self.data['current_station']['station']
    
    def status(self):
        return self.data['current_station']['status']
    
    def sch_arrival(self):
        return self.data['current_station']['scharr']
    
    def sch_departure(self):
        return self.data['current_station']['schdep']
    
    def act_arrival(self):
        return self.data['current_station']['actarr']
    
    def act_departure(self):
        return self.data['current_station']['actdep']
    
    def late_by_minutes(self):
        return self.data['current_station']['latemin']
    
    def sch_arr_date(self):
        return self.data['current_station']['scharr_date']
    
    def act_arr_date(self):
        return self.data['current_station']['actarr_date']
    
    def distance_travelled(self):
        return self.data['current_station']['distance']
    
    def has_arrived(self):
        return self.data['current_station']['has_arrived']
    
    def has_departed(self):
        return self.data['current_station']['has_departed']
    
    def train_start_date(self):
        return self.data['start_date']
    
    def train_position(self):
        return self.data['position']
    
    def train_number(self):
        return self.data['train']['number']
    
    def train_name(self):
        return self.data['train']['name']
    
    def response_code(self):
        return self.data['response_code']



class GetStationsByCode():
    
    def __init__(self,stn_code):
        self.stn_code = str(stn_code)
        self.data = self.get_stations()
    
    def get_stations(self):
        req = requests.get('http://api.railwayapi.com/v2/code-to-name/code/{}/apikey/{}/'.format(self.stn_code,api_key))
        data = req.json()
        return data


def response_code(self):
    return self.data['response_code']
    
    def stations_list(self):
        return self.data['stations']

class TrainRunningDetailsByNumber():
    
    def __init__(self,train_no):
        self.train_no = str(train_no)
    
    def get_stations(self):
        req = requests.get('http://api.railwayapi.com/v2/name-number/train/{}/apikey/{}/'.format(self.train_no,api_key))
        self.data = req.json()
    #return data
    
    def days_list(self):
        return self.data['train']['days']
    
    def response_code(self):
        return self.data['response_code']
    
    def train_name(self):
        return self.data['train']['name']
    
    def train_number(self):
        return self.data['train']['number']


class RescheduledTrains():
    
    def __init__(self,date):
        self.date = str(date)
        self.data = self.get_rescheduled_trains()
    
    def get_rescheduled_trains(self):
        req = requests.get('http://api.railwayapi.com/v2/rescheduled/date/{}/apikey/{}/'.format(self.date,api_key))
        data = req.json()
        return data
    
    def response_code(self):
        return self.data['response_code']
    
    def trains_details(self):
        return self.data['trains']

class CancelledTrains():
    
    def __init__(self,date):
        self.date = str(date)
        self.data = self.get_cancelled_trains()
    
    def get_cancelled_trains(self):
        req = requests.get('http://api.railwayapi.com/v2/cancelled/date/{}/apikey/{}/'.format(self.date,api_key))
        data = req.json()
        return data
    
    def response_code(self):
        return self.data['response_code']
    
    def trains_details(self):
        return self.data['trains']
    
    def last_updated(self):
        return self.data['last_updated']

class TrainInfo():
    
    def __init__(self,train_no):
        self.train_no = str(train_no)
        self.data = self.get_train_info()
    
    def get_train_info(self):
        req = requests.get('http://api.railwayapi.com/v2/route/train/{}/apikey/{}/'.format(self.train_no,api_key))
        data = req.json()
        return data
    
    
    def response_code(self):
        return self.data['response_code']
    
    def train_route(self):
        return self.data['route']
    
    def train_number(self):
        return self.data['train']['number']
    
    def train_name(self):
        return self.data['train']['name']
    
    def train_classes(self):
        return self.data['train']['classes']
    
    def train_days(self):
        return self.data['train']['days']


class SeatAvailability():
    
    def __init__(self,train_no,stn_code,dest_code,date,class_code,quota_code):
        self.train_no = str(train_no)
        self.stn_code = str(stn_code)
        self.dest_code = str(dest_code)
        self.date = str(date)
        self.class_code = str(class_code)
        self.quota_code = str(quota_code)
        self.data = self.get_seat_availability()
    
    def get_seat_availability(self):
        req = requests.get('http://api.railwayapi.com/v2/check-seat/train/{}/source/{}/dest/{}/date/{}/class/{}/quota/{}/apikey/{}/'.format(self.train_no,self.stn_code,self.dest_code,self.date,self.class_code,self.quota_code,api_key))
        data = req.json()
        return data
    
    
    def response_code(self):
        return self.data['response_code']
    
    def from_code(self):
        return self.data['from_station']['code']
    
    def from_name(self):
        return self.data['from_station']['name']
    
    def to_code(self):
        return self.data['to_station']['code']
    
    def to_name(self):
        return self.data['to_station']['name']
    
    def quota_name(self):
        return self.data['quota']['name']
    
    def quota_code(self):
        return self.data['quota']['code']
    
    def train_number(self):
        return self.data['train']['number']
    
    def train_name(self):
        return self.data['train']['name']
    
    def journey_class_name(self):
        return self.data['journey_class']['name']
    
    def journey_class_code(self):
        return self.data['journey_class']['code']
    
    
    
    def class_name(self):
        return self.data['class']['name']
    
    def class_code(self):
        return self.data['class']['code']
    
    def availability(self):
        return self.data['availability']

class TrainBetweenStations():
    
    def __init__(self,stn_code,dest_code,date):
        self.stn_code = str(stn_code)
        self.dest_code = str(dest_code)
        self.date = str(date)
        self.data = self.train_btw_stations()
    
    def train_btw_stations(self):
        req = requests.get('http://api.railwayapi.com/v2/between/source/{}/dest/{}/date/{}/apikey/{}/'.format(self.stn_code,self.dest_code,self.date,api_key))
        data = req.json()
        return data
    
    def response_code(self):
        return self.data['response_code']
    
    def total_trains_found(self):
        return self.data['total']
    
    def trains_details(self):
        return self.data['trains']


class CheckFare():
    
    def __init__(self,train_no,stn_code,dest_code,age,quota_code,date):
        self.train_no = str(train_no)
        self.stn_code = str(stn_code)
        self.dest_code = str(dest_code)
        self.age = age
        self.quota_code = str(quota_code)
        self.date = str(date)
        self.data = self.get_fare()
    
    
    def get_fare(self):
        req = requests.get('http://api.railwayapi.com/v2/fare/train/{}/source/{}/dest/{}/age/{}/quota/{}/date/{}/apikey/{}/'.format(self.train_no,self.stn_code,self.dest_code,self.age,self.quota_code,self.date,api_key))
        data = req.json()
        return data
    
    def response_code(self):
        return self.data['response_code']
    
    def from_code(self):
        return self.data['from_station']['code']
    
    def from_name(self):
        return self.data['from_station']['name']
    
    def to_code(self):
        return self.data['to_station']['code']
    
    def to_name(self):
        return self.data['to_station']['name']
    
    def quota_name(self):
        return self.data['quota']['name']
    
    def quota_code(self):
        return self.data['quota']['code']
    
    def train_number(self):
        return self.data['train']['number']
    
    def train_name(self):
        return self.data['train']['name']
    
    def fare_details(self):
        return self.data['fare']


'''
    #temp check
    train = LiveTrain('12688','18-08-2017')
    l = train.status()
    print(l)
    '''
'''
    ct = CancelledTrains('18-08-2017')
    l = ct.get_cancelled_trains()
    print(l)
    '''
