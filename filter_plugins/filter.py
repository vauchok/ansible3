def get_mongo_src(arg, os_family, os_release, mongodb_version):
	if os_family == 'RedHat':
		os_family = 'rhel'
	elif os_family == 'Debian':
		os_family = 'debian'
	elif os_family == 'SLES':
		os_family = 'sles'    
	for i in arg:
        	if os_family in i and os_release in i and mongodb_version in i:
            		return i

class FilterModule(object):
    def filters(self):
        return {
            'get_mongo_src': get_mongo_src
        }
