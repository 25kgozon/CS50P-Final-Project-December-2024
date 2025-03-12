from project import *
import pytest

def test_gen_rand_european_dish(mocker):
    mocker.patch("project.read_csv", return_value=["Recipe 1", "Recipe 2", "Recipe 3"])
    mock_gen_pdf = mocker.patch("project.gen_pdf", return_value="Recipe 1")
    gen_rand_european_dish()
    mock_gen_pdf.assert_called_once()


def test_gen_rand_latin_dish(mocker):
    mocker.patch("project.read_csv", return_value=["Recipe 1", "Recipe 2", "Recipe 3"])
    mock_gen_pdf = mocker.patch("project.gen_pdf", return_value="Recipe 1")
    gen_rand_latin_dish()
    mock_gen_pdf.assert_called_once()


def test_gen_rand_african_dish(mocker):
    mocker.patch("project.read_csv", return_value=["Recipe 1", "Recipe 2", "Recipe 3"])
    mock_gen_pdf = mocker.patch("project.gen_pdf", return_value="Recipe 1")
    gen_rand_african_dish()
    mock_gen_pdf.assert_called_once()



