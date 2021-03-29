pragma solidity ^0.4.0;

contract Election {
    
    struct Canditate {
        string name;
        uint voteCount;
    }
    
    struct Voter {
        bool voted;
        uint voterIndex;
        uint weigth;
    }
    
    address public owner;
    string public name;
    mapping(address => Voter) public voters;
    Canditate[] public canditates;
    uint public auctionEnd;
    
    event ElectionResult (string name, uint voteCount);
    
    function Election (string _name, uint duraitonMinutes, string canditate1, string canditate2) {
            owner = msg.sender;
            name = _name;
            auctionEnd = now + (duraitonMinutes *1 minutes);
            
            canditates.push(Canditate(canditate1, 0));
            canditates.push(Canditate(canditate2, 0));
    }
    
    function authorize(address voter) public {
        require(msg.sender == owner);
        require(!voters[voter].voted);
        voters[voter].weigth = 1;
    }
    
    function vote(uint voterIndex) public {
        require (now < auctionEnd);
        require (!voters[msg.sender].voted);
        
        voters[msg.sender].voted = true;
        voters[msg.sender].voterIndex = voterIndex;
        
        canditates[voterIndex].voteCount == voters[msg.sender].weigth;
    }
    
    function end() public {
        require (msg.sender == owner);
        require (now >= auctionEnd);
        
        for (uint i=0; i<canditates.length; i++) {
            ElectionResult(canditates[i].name, canditates[i].voteCount);
        }
    }
    
}
