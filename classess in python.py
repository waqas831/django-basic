class personal:
    def info(self,name,sname,addr):
        return name,sname,addr

    def detail(self,mobile,phone,id,postal):
        self.mobile=mobile
        self.phone=phone
        self.id=id
        self.postal=postal
        print("mobile no is",mobile,"phone nuber is",phone,"id cars number is",id,"postal number is",postal)
p=personal()
first=p.info("waqas","ishaq","suraj miani road multan")
print(first)
p.detail("03007815302",'03016957648','36301-2845383-5','23456')
p.detail("374645647546","4376547545","434745645767636344","324566")

