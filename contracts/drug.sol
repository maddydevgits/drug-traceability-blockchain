// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract drug {
  
  address[] _labmanu;
  string[] _labform;
  string[][] _labfeeds;

  mapping(string=>bool) labmanus;

  function addLabManufacturer(address labmanu,string memory labform) public {

    labmanus[labform]=true;
    _labmanu.push(labmanu);
    _labform.push(labform);
    _labfeeds.push(["Nice Job"]);
  }

  function viewLabManufacturers() public view returns(address[] memory,string[] memory) {
    return (_labmanu,_labform);
  }

  function addLabFeedback(uint labform,string memory feed) public {  
    _labfeeds[labform].push(feed);          
  }

  function viewLabFeedback() public view returns(string[][] memory) {
    return (_labfeeds);
  }
}
