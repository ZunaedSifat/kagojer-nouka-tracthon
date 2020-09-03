from api import models


class ClusterCache:
    __instance = None

    @staticmethod
    def get_instance():
        if not ClusterCache.__instance:
            ClusterCache.__instance = ClusterCache()
        return ClusterCache.__instance

    @staticmethod
    def get_words(keywords):
        return sorted([keyword.word for keyword in keywords])

    def __init__(self):
        if ClusterCache.__instance:
            raise Exception("This is a singleton class")
        self.data = {}
        for item in models.Cluster.objects.all():
            self.data[item.id] = ClusterCache.get_words(item.keywords.all())

    def set(self, key, cluster):
        self.data[key] = sorted(ClusterCache.get_words(cluster.keywords.all()))

    def get(self, key):
        return self.data.get(key)

    def create(self, keywords):
        instance = models.create_cluster_from_keywords(keyword_list=keywords)
        self.set(instance.id, cluster=instance)

    def is_present(self, keywords):
        return ClusterCache.get_words(keywords) in self.data.values()


class KeywordCache:
    __instance = None

    @staticmethod
    def get_instance():
        if not KeywordCache.__instance:
            KeywordCache.__instance = KeywordCache()
        return KeywordCache.__instance

    def __init__(self):
        if KeywordCache.__instance:
            raise Exception("This is a singleton class")
        self.data = {}
        for item in models.Keyword.objects.all():
            if item.word not in self.data:
                self.data[item.word] = set()
            self.data[item.word].add(item.content.id)

    def set(self, keyword):
        if keyword.word not in self.data:
            self.data[keyword.word] = set()
        self.data[keyword.word].add(keyword.content.id)

    def get(self, key):
        return self.data.get(key)

    def count(self, keyword_list):
        result = self.data.get(keyword_list[0].word)
        for keyword in keyword_list:
            result = result.intersection(self.data.get(keyword.word))
        return len(result)
