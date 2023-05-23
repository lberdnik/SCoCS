class JsonSerializer:
    
    @classmethod
    def load(cls, file):
        return cls.loads(file.read())

    @classmethod
    def loads(cls, file):
        pass
    
    @classmethod
    def dump(cls, obj, file):
        file.write(cls.dumps(obj))

    @classmethod
    def dumps(cls, file):
        pass