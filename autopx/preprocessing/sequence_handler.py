# autopx/preprocessing/sequence_handler.py

from autopx.utils.constants import ModelType
# Note: In a real environment, tensorflow would need to be installed.
# We will use a fallback or ensure it's imported if possible.
try:
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    from tensorflow.keras.preprocessing.text import Tokenizer
except ImportError:
    # Minimal mock if TF is not available
    def pad_sequences(sequences, maxlen=None, padding='post', truncating='post'):
        return sequences # Mock
    class Tokenizer:
        def __init__(self, **kwargs): pass
        def fit_on_texts(self, texts): pass
        def texts_to_sequences(self, texts): return [list(range(len(t.split()))) for t in texts]

class SequenceHandler:
    """
    Handles sequence preparation for deep learning and transformer models.
    """

    def __init__(self, max_len=None, oov_token="<OOV>"):
        """
        :param max_len: maximum sequence length (optional). If None, auto-detect.
        :param oov_token: token for out-of-vocabulary words
        """
        self.max_len = max_len
        self.tokenizer = Tokenizer(oov_token=oov_token)
    
    def fit_tokenizer(self, texts):
        """
        Fit the tokenizer on the given texts.
        """
        self.tokenizer.fit_on_texts(texts)
        return self

    def texts_to_sequences(self, texts):
        """
        Convert texts to integer sequences.
        """
        return self.tokenizer.texts_to_sequences(texts)

    def pad_sequences(self, sequences, padding='post', truncating='post'):
        """
        Pad or truncate sequences to max_len.
        If max_len not specified, use the length of the longest sequence.
        """
        if not self.max_len:
            if sequences:
                self.max_len = max(len(seq) for seq in sequences)
            else:
                self.max_len = 0
        return pad_sequences(sequences, maxlen=self.max_len, padding=padding, truncating=truncating)

    def fit_transform(self, texts):
        """
        Fit the tokenizer and return padded sequences.
        """
        self.fit_tokenizer(texts)
        sequences = self.texts_to_sequences(texts)
        padded = self.pad_sequences(sequences)
        return padded
