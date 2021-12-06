import { useState } from "react";
import styled from "styled-components";
const List = styled.li`
// display: inline-block;
`
export default function Option({item, checkedHandler}) {
    const [bChecked, setChecked] = useState(false);
    const setPurpose = (e) => {
        console.log(e)
    }
    return (
        <>
            <List>
                <input
                    type="checkbox"
                    id={item.id}
                    onChange={checkedHandler}
                    name="type"
                />
                &nbsp;{item.type}&nbsp;
                <li className="purpose-li">
                    <div className="purpose-box">
                        <button
                            type="button"
                            className=" purpose"
                            onClick={setPurpose}
                        >
                            {item.type}
                        </button>
                    </div>
                </li>
            </List>
        </>
    );
}