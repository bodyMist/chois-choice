import { useState } from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";
import list from "./purpose.json";
import Option from "./Option"

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
    const checkedItemHandler = (id, isChecked) =>{
        if(isChecked)
            console.log(id);
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
                            <Option id={item.id} checkedItemHandler={checkedItemHandler} type={item.type}/>
                        </List>
                    );
                })}
                
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
