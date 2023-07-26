function compile_and_run(file_name, options)
    pyrunfile("translate.py")

    opt_str = "";
    for opt=options
        opt_str = opt_str + "," + opt + "=True";
    end

    run_str = "import translate; " + "translate.translate('" + file_name + "'" + opt_str + ")";
    pyrun(run_str)

    matlab
end