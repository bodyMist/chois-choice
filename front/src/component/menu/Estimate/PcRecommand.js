import { Link } from "react-router-dom";
import styled from "styled-components";
import list from "./purpose.json";

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
    return (
        <div className="container">
            {/* <h3>PC 견적 추천</h3> */}
            <Link to="/Estimate">견적 작성</Link>
            {/* <div className="input-group-pc">
                <input
                    type="text"
                    className="form-control"
                    placeholder="예산 입력"
                ></input>
                <input
                    type="text"
                    className="form-control second"
                    placeholder="용도 입력"
                ></input>
                <button className="btn btn-default">제출</button>
            </div> */}
            <InputGroupPc>
                <FormControl
                    type="text"
                    placeholder="예산 입력(원)"
                ></FormControl>
                <ul>
                {list.menus.map((item)=>{
                    return (
                        <List>
                            <input type="checkbox" id={item.id} />
                            &nbsp;{item.type}&nbsp;
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
