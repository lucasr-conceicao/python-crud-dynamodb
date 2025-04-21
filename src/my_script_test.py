from src import my_script


def test_main(capsys):
    my_script.main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, world!"
