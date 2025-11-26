# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from typing import List, Optional
from openapi_server.models.article import Article


class BaseShopApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseShopApi.subclasses = BaseShopApi.subclasses + (cls,)
    async def articles_get(
        self,
    ) -> List[Article]:
        """Articles will be provided"""
        ...


    async def articles_post(
        self,
        article: Optional[Article],
    ) -> Article:
        """This is an **article**  It consist of:   - name   - price   - id  Inline-style:  ![alt text](https://www.workingsoftware.dev/content/images/2022/12/image-75.png \&quot;Logo Title Text 1\&quot;)  | Tables        | Are           | Cool  | | ------------- |:-------------:| -----:| | col 3 is      | right-aligned | $1600 | | col 2 is      | centered      |   $12 | | zebra stripes | are neat      |    $1 | """
        ...
