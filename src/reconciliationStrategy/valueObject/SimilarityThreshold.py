class SimilarityThreshold:
    def __init__(self, percentage) -> None:
        if percentage > 100 or percentage < 0:
            raise Exception("invalid percentage it should be between 0 and 100")
        self.percentage = percentage
        
    def __eq__(self, otherSimilarityThreshold:"SimilarityThreshold"):
        if isinstance(otherSimilarityThreshold, SimilarityThreshold):
            return self.percentage == otherSimilarityThreshold.percentage
        return False

    def __gt__(self, otherSimilarityThreshold:"SimilarityThreshold"):
        if isinstance(otherSimilarityThreshold, SimilarityThreshold ):
            return self.percentage > otherSimilarityThreshold.percentage
        return NotImplemented

