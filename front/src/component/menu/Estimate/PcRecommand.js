import { useState } from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";
import list from "./purpose.json";
import Detail from "./Detail"
import Option from "./Option";
import axios from "axios";
import Result from "./Result";

const InputGroupPc = styled.div`
display: flex;
flex-direction: row;
white-space: nowrap;
vertical-align: middle;
border-collapse: separate;
align-content: center;
justify-content:center;
`;
const FormControl = styled.input`
position: relative;
width: 100%;
max-width: 300px;
`;

const SubmitBtn = styled.button`
margin-left: -1px;
white-space: unset;
height: 34px;
display: inline-block;
padding: 6px 12px;
margin-bottom: 0;
font-size: 14px;
font-weight: normal;
text-align: center;
vertical-align: middle;
cursor: pointer;
user-select: none;
background-image: none;
border: 1px solid transparent;
border-radius: 0;
`;
const List = styled.li`
// display: inline-block;
`
const Container = styled.div `
display:flex;
flex-direction:column;
align-items: center;
`

const ResultBox = styled.div `
    display: ${props=>props.name == true ? "flex" : "none"};
    flex-direction: column;
    align-items: center;
`
export default function PcRecommand() {
const [selected, setSelected] = useState([{"selected":1}, {"selected":0}, {"selected":0}]);
const [detail, setDetail] = useState([{"selected":0}, {"selected":0}, {"selected":0}, {"selected":0}])
const [data, setData] = useState(new Set());
const [list, setList] = useState([{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}])
const [load, setLoad] = useState(false);
const setPurpose = (e) => {
    const id = e.target.id;
    let select =[
        {"selected":0}, {"selected":0}, {"selected":0}
    ]
    select[id-1].selected=1;
    setSelected(select)
}
const setDetailPurpose = (e) =>{
    const id = e.target.id;
    const name = e.target.name;

    let select = [...detail];
    if(detail[id-1].selected == 0) {
        select[id-1].selected = 1;
        data.add(name);
        setData(data);
    } 
    else {
        select[id-1].selected = 0;
        data.delete(name);
        setData(data);
    }
    setDetail([...select]);
    console.log(data)
}
const sendData =(e)=>{
    const budget = document.getElementById("budge").value;
    const uses = [...data];
    console.log(uses)
    // console.log(params);
    axios.get(`/estimate/`,{ params: {uses, budget} })
    .then((response)=>{
        setList(response.data);
        setLoad(true);
        console.log(response);
    })
    .catch((e)=>{
        console.error(e);
    });
}
return (
    <div className="container">
        <Link to="/Estimate">견적 작성</Link>
        <Container>
            <FormControl
                id="budge"
                type="text"
                placeholder="예산 입력(원)"
            ></FormControl>
            <InputGroupPc>
                <ul className="purpose-ul">
                    <li className="purpose-li">
                        <div className= {(selected[0].selected == 1 ? "Selected" : '')+" purpose-box"}>
                            <button type="button" className=" purpose" onClick={setPurpose} id="1">
                                게임
                            </button>
                        </div>
                    </li>
                    <li className="purpose-li">
                        <div className={(selected[1].selected == 1 ? "Selected" : '')+" purpose-box"}>
                            <button type="button" className=" purpose" onClick={setPurpose} id="2">
                                사무용
                            </button>
                        </div>
                    </li>
                    <li className="purpose-li">
                        <div className={(selected[2].selected == 1 ? "Selected" : '')+" purpose-box"}>
                            <button type="button" className=" purpose" onClick={setPurpose} id="3">
                                딥러닝
                            </button>
                        </div>
                    </li>
                </ul>
                <ul className="detail-purpose-ul">
                    <div className = {(selected[0].selected == 1 ? "Selected" : '')+" detail"}>
                        <li className="detail-purpose-li">
                            <div className={(detail[0].selected==1?"Selected":'')+" detail-purpose-box"}>
                                <button type="button" className="detail-purpose-btn" onClick={setDetailPurpose} id="1" name="battleground">
                                    배그
                                </button>
                            </div>
                        </li>
                        <li className="detail-purpose-li">
                            <div className={(detail[1].selected==1?"Selected":'')+" detail-purpose-box"}>
                                <button type="button" className="detail-purpose-btn" onClick={setDetailPurpose} id="2" name="lol">
                                    롤
                                </button>
                            </div>
                        </li>
                    </div>
                    <div className = {(selected[1].selected == 1 ? "Selected" : '')+" detail"}>
                        <li className="detail-purpose-li">
                            <div className={(detail[2].selected==1?"Selected":'')+" detail-purpose-box"}>
                                <button type="button" className="detail-purpose-btn" onClick={setDetailPurpose} id="3" name="internet">
                                    인터넷 서핑
                                </button>
                            </div>
                        </li>
                        <li className="detail-purpose-li">
                            <div className={(detail[3].selected==1?"Selected":'')+" detail-purpose-box"}>
                                <button type="button" className="detail-purpose-btn" onClick={setDetailPurpose} id="4" name="office">
                                    문서 작업
                                </button>
                            </div>
                        </li>
                    </div>
                </ul>
            </InputGroupPc>
            <SubmitBtn type="button" onClick={sendData} >
                제출
            </SubmitBtn>
        </Container>
        {/* <div className="result-box">
            <h5>결과</h5>
            <Result list={list}/>
        </div> */}
        <ResultBox name={load}>
            <h5>결과</h5>
            <Result list={list}/>
        </ResultBox>
    </div>
);
}
