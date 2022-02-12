vector<int> zadanie2(string sciezka) {
    fstream plik;
    plik.open(sciezka, ios::in| ios::out);

    string linia;
    vector<string> lines;


    while (getline(plik, linia)) {
        lines.push_back(linia);
    }

    int x = lines[0][0];
    int y = lines[0][2];
    int z = lines[0][4];

    vector<vector<int>> portale;

    int pozX = 0;
    int pozY = 0;
    int pozZ = 0;

    for (int i=1; i<lines.size(); i++) {
        for (int j=0; j<x; j++) {
            if (lines[i][j] == '$') {
                pozX = j;
                pozY = (i-1)%4;
                pozZ = (i-1)/4;
            }   else if(lines[i][j] == 'P') {
                portale.push_back({j, (i-1)%4, (i-1)/4});
            }
        }
    }

    double minOdl;
    double odl;
    vector<int> wsp;

    for (int i=0; i<portale.size(); i++) {
        odl = sqrt(pow(pozX-portale[i][0], 2) + pow(pozY-portale[i][1], 2) + pow(pozZ-portale[i][2], 2));
        if (i==0 || odl<minOdl) {
            minOdl = odl;
            wsp = portale[i];
        }
    }

    return wsp;
}
