import { useState } from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";
import list from "./purpose.json";
import Option from "./Option"
import Detail from "./Detail"

const InputGroupPc = styled.div`
    display: flex;
    flex-direction: column;
    white-space: nowrap;
    vertical-align: middle;
    border-collapse: separate;
    align-items: center;
`;
const FormControl = styled.input`
    position: relative;
    width: 500px;
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
display: inline-block;
`
export default function PcRecommand() {
    console.log(list.purpose)
    const [detail, setDetail] = useState([])
    const checkedHandler = (e) => {
        const id = e.target.id
        const checkboxes = document.getElementsByName("type");
        checkboxes.forEach((cb)=>{
            cb.checked=false;
        })
        e.target.checked = true;
        if(id!=3) {
            const sdetail = list.purpose[id-1]
            setDetail([...sdetail])
        }
        console.log(e.checked)
        console.log(detail)
    }
    return (
        <div className="container">
            <Link to="/Estimate">견적 작성</Link>

            <InputGroupPc>
                <FormControl
                    type="text"
                    placeholder="예산 입력(원)"
                ></FormControl>
                <ul>
                {list.menus.map((item)=>{
                    return (
                        <List>
                            <input
                                type="checkbox"
                                id={item.id}
                                onChange={checkedHandler}
                                name="type"
                            />
                            &nbsp;{item.type}&nbsp;
                        </List>
                    );
                })}
                
                </ul>
                <ul>
                {detail.map((item)=>(
                    <List>
                        <Detail id={item.id} name={item.name}/>
                    </List>
                ))}
                </ul>
                <SubmitBtn>제출</SubmitBtn>
            </InputGroupPc>
            <div className="text-center">
                <h5>결과</h5>
                <span></span>
            </div>
        </div>
    );
}
