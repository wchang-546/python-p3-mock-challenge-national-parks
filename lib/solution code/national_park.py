class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []
    
    @property
    def name(self): 
        return self._name 
    
    @name.setter
    def name(self, value):
        if value and isinstance (value, str) and not hasattr(self, "name"):
            self._name = value
        else:
            raise Exception

    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if new_visitor and isinstance(new_visitor, Visitor) and new_visitor not in self._visitors: 
            self._visitors.append(new_visitor)
        return self._visitors
    
    def total_visits(self):
        return len(self._trips)
    
    def best_visitor(self):
        max_visits = 0
        max_visitor = None 
        for visitor in self._visitors: 
            visitor_visits = len([res for res in self._trips if res.visitor == visitor])
            if visitor_visits > max_visits:
                max_visits = visitor_visits
                max_visitor = visitor 
        return max_visitor