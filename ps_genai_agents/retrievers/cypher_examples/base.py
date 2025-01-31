from abc import ABC, abstractmethod
from typing import List

from pydantic import BaseModel


class BaseCypherExampleRetriever(BaseModel, ABC):
    """
    Abstract base class for an example retriever.
    Subclasses must implement the `get_examples` method.
    """

    @abstractmethod
    def get_examples(self) -> str:
        """
        Retrieve relevant examples in string format that are ready to be injected into a prompt for few shot prompting.

        Returns
        -------
        str
            A list of examples as a string.
        """
        pass
