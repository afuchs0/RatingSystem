class User:
    def _init_(self, id, nome,voting,prefgenre,eta):
        self.id = id
        self.nome = nome
        self.voting = voting
        self.prefgenre = prefgenre
        self.eta = eta
    def add_val(self,key, value):
        self.voting[key] = value
    def add_pref(self,gen):
        self.prefgenre.append(gen)
