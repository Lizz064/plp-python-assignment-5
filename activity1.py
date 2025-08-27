# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"Device: {self.brand} {self.model}"

# Child Class
class Smartphone(Device):   
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  
        self.os = os
        self.storage = storage
        self.battery = 100 
    
    # Method to display phone info
    def phone_info(self):
        return f"{self.device_info()} | OS: {self.os}, Storage: {self.storage}GB, Battery: {self.battery}%"
    
    # Simulate using the phone
    def use_phone(self, hours):
        drain = hours * 10
        if drain > self.battery:
            self.battery = 0
            return "Battery drained! Please charge your phone."
        else:
            self.battery -= drain
            return f"Used phone for {hours}h. Battery now at {self.battery}%."
    
    # Charge the phone
    def charge(self):
        self.battery = 100
        return "Phone fully charged to 100%."

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S23", "Android", 256)
phone2 = Smartphone("Apple", "iPhone 14", "iOS", 128)

# Test methods
print(phone1.phone_info())
print(phone1.use_phone(3))
print(phone1.phone_info())
print(phone1.charge())
print(phone2.phone_info())
