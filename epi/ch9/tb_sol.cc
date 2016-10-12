#include<iostream>
#include<vector>
#include<string>
#include<stdexcept>

using namespace std;

string ShortestEquivalentPath(const string& path) 
{
    if (path.empty())
        throw invalid_argument("Empty string is not a valid path!");

    vector<string> path_names;
    if(path.front() == '/')
        path_names.emplace_back('/');

    stringstream ss(path);


    string token;

    while(getline(ss, token, '/')) {
        if (token == "..") {
            if(path_names.empty() || path_names.back() == "..") {
                path_names.emplace_back(token);
            } else {
                if(path_names.back() == 'ZZ
            }
        }
    }


}
