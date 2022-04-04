from django.test import TestCase
import requests
import os
from .PaperProcessor.PaperProcessor import PaperProcessor

# Create your tests here.
# Written by Minyi Lei
class BasicTest(TestCase):
    def setUp(self) -> None:
        with open("test_shapes.pdf","wb") as f:
            content=requests.get("https://earlbarr.com/publications/shapes.pdf").content
            f.write(content)
        self.pp=PaperProcessor("test_shapes.pdf")

    def tearDown(self) -> None:
        os.remove("test_shapes.pdf")

    def testKeyword(self):
        result=self.pp.wordFrequency(max=100,ignoreCase=False,useLemma=True)
        self.assertEqual(result["object"],146)
        self.assertEqual(result["Java"],11)
        self.assertEqual(result["structure"],67)

    def testMeta(self):
        result=self.pp.metaData()
        self.assertEqual(result["title"],"Collecting a Heap of Shapes")

    def testReferences(self):
        result=self.pp.references()
        self.assertEqual(len(result),33)
    
    def testSections(self):
        result=self.pp.sections()
        self.assertEqual(len(result),11)
    