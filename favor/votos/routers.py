class RoutersDataBase(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'votos':
            return 'mongodb'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'votos':
            return 'mongodb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        pass

    def allow_syncdb(self, db, model):
        if db == 'mongodb':
            print model._meta.app_label
            print model._meta.app_label == 'votos'
            return model._meta.app_label == 'votos'
        elif model._meta.app_label == 'votos':
            print model._meta.app_label
            return False 
        return None