// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract register {
  string[] _names;
  uint[] _roles;
  address[] _users;
  uint[] _passwords;

  mapping(address=>bool) users;

  constructor()  {
  }

  function registerUser(address user,uint password,string memory name,uint role) public {

    require(!users[user]);
    _users.push(user);
    _passwords.push(password);
    _names.push(name);
    _roles.push(role);
  }

  function loginUser(address user,uint password) public view returns (bool) {
    uint i;

    for(i=0;i<_users.length;i++) {
      if(user==_users[i] && _passwords[i]==password) {
        return true;
      }
    }
    return false;
  }

  function viewUsers() public view returns(address[] memory,uint[] memory,uint[] memory,string[] memory) {
    return (_users,_passwords,_roles,_names);
  }
}
