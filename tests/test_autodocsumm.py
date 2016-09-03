import sys
import os.path as osp
import unittest
from sphinx_testing import with_app


sys.path.insert(0, osp.abspath('sphinx_supp'))


class TestAutosummaryDocumenter(unittest.TestCase):

    @with_app(buildername='html', srcdir='sphinx_supp',
              copy_srcdir_to_tmpdir=True)
    def test_module(self, app, status, warning):
        app.build()
        html = (app.outdir / 'test_module.html').read_text()
        self.assertIn('<span class="pre">TestClass</span>', html)
        self.assertIn('<span class="pre">test_func</span>', html)
        self.assertIn('<span class="pre">test_method</span>', html)
        self.assertIn('<span class="pre">test_attr</span>', html)
        self.assertIn('<span class="pre">class_caller</span>', html)
        self.assertIn('Caller docstring for class attribute', html)

        # test whether the data is shown correctly
        self.assertIn('<span class="pre">large_data</span>', html)
        self.assertIn('<span class="pre">small_data</span>', html)

        self.assertNotIn('Should be skipped', html)
        self.assertIn('Should be included', html)

        self.assertNotIn('Should also be skipped', html)
        self.assertIn('Should also be included', html)

    @with_app(buildername='html', srcdir='sphinx_supp',
              copy_srcdir_to_tmpdir=True)
    def test_class(self, app, status, warning):
        app.build()
        html = (app.outdir / 'test_class.html').read_text()
        self.assertIn('<span class="pre">test_method</span>', html)
        self.assertIn('<span class="pre">test_attr</span>', html)
        self.assertIn('<span class="pre">class_caller</span>', html)
        self.assertIn('Caller docstring for class attribute', html)

        # test whether the data is shown correctly
        self.assertIn('<span class="pre">large_data</span>', html)
        self.assertIn('<span class="pre">small_data</span>', html)

        self.assertNotIn('Should be skipped', html)
        self.assertIn('Should be included', html)


if __name__ == '__main__':
    unittest.main()