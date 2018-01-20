def convert_file(input_file,out_file):
  in_lines = open(input_file).readlines()
  out_file = open(out_file,"w")
  out_file.write(in_lines[0]+"\n")
  for line in in_linest:
    spl_line = line.split(",")
    mol = spl_line[0]
    main_frag = sorted(mol.split("."),reverse=True)[0]
    main_frag = '"'+main_frag+'"\n'
    spl_line[0] = main_frag
    out_file.write(",".join(spl_line)+"\n")
  out_file.close()
