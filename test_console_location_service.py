from console_location_service import ConsoleLocationService

service = ConsoleLocationService()

service.store('user-1', 'Budapest', 'Hungary')
service.store('user-2','Berlin', 'Germany')
service.store('user-3', 'Berlin', 'Germany')
service.store('user-4','London', 'UK')
service.store('user-4','Budapest', 'Hungary')

print('Listing by name')
print(service.list_by_name('user-1'))

print('Listing by location')
print(service.list_by_location('Berlin','Germany'))

print('Remove')
service.remove('user-4')
print(service.list_by_name('user-4'))

