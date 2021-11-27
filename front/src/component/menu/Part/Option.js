import { useState } from "react";

export default function Option({ key, title, checkedItemHandler, id }) {
    const [bChecked, setChecked] = useState(false);
    const checkedHandler = (e) => {
        setChecked(!bChecked);
        const name = e.target.name
        const id = e.target.id
        const inf = {name, id};

        checkedItemHandler(inf, e.target.checked);
    }
    return (
        <>
            <li className="sub_item" key={key}>
                <label title={title}>
                    <input type="checkbox" title={title} checked={bChecked} onChange={checkedHandler} id={id}/>
                    &nbsp;{title}&nbsp;
                </label>
            </li>
        </>
    );
}
