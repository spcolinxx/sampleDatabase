from flask_script import Manager

from sampleDatabase import app
from flask_migrate import Migrate,MigrateCommand
from exts import ormdb

# 注意要将数据库模型import一下，否则无效
from models import SampleInfo,OrgInfo,DonorInfo,ProjectInfo,Cate_code

manager=Manager(app)

migrate=Migrate(app,ormdb)

manager.add_command('db_command',MigrateCommand)

if __name__=='__main__':
    manager.run()