{ pkgs }: {
  SystemPackages = with pkgs; [
    cowsay
    requests
    autopep8
    black
    blinker
    click
    flask
    itsdangerous
    packaging
    pathspec
    platformdirs
    pycodestyle
    pyflakes
    PyQt5
    PyQt5-sip
    PyQtWebEngine-Qt5
    tomli
    typing-extensiona
    wekzeug
    
  ];
  deps = [
    pkgs.vercel-pkg
    pkgs.pkg
  ];
}
