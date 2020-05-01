spain = input()
electric = input()
strange = ["Strange", "Quark", "1/2", "-1/3"]
charm = ["Charm", "Quark", "1/2", "2/3"]
electron = ["Electron", "Lepton", "1/2", "-1"]
muon = ["Muon", "Lepton", "1/2", "0"]
photon = ["Photon", "Boson", "1", "0"]
higgs_boson = ["Higgs boson", "Boson", "0", "0"]

if spain == strange[2] and electric == strange[3]:
    print(strange[0] + " " + strange[1])
elif spain in charm and electric in charm:
    print(charm[0] + " " + charm[1])
elif spain == electron[2] and electric == electron[3]:
    print(electron[0] + " " + electron[1])
elif spain == muon[2] and electric == muon[3]:
    print(muon[0] + " " + muon[1])
elif spain == photon[2] and electric == photon[3]:
    print(photon[0] + " " + photon[1])
elif spain == higgs_boson[2] and electric == higgs_boson[3]:
    print(higgs_boson[0] + " " + higgs_boson[1])