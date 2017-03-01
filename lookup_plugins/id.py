import os
import pwd

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):
    supported_prop = {
       'uid': os.getuid,
       'euid': os.geteuid,
       'uname': lambda:pwd.getpwuid(os.getuid()).pw_name,
       'euname': lambda:pwd.getpwuid(os.geteuid()).pw_name,
    }

    def run(self, terms, variables, **kwargs):

        ret = []
        for term in terms:
            term = str(term)

            if LookupModule.supported_prop.get(term) is None:
                raise AnsibleError("lookup_plugin.id(%s) is not supported" % (term))

            ret.append(LookupModule.supported_prop.get(term)())
        return ret
