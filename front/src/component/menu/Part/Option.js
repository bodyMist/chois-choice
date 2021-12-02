import { useState } from "react";

export default function Option({ title, checkedItemHandler, id }) {
    const [bChecked, setChecked] = useState(false);
    const checkedHandler = (e) => {
        setChecked(!bChecked);
        const title = e.target.title
        const id = e.target.id

        checkedItemHandler(title, e.target.checked);
    }
    return (
        <>
            <li className="sub_item">
                <label title={title}>
                    <input type="checkbox" title={title} checked={bChecked} onChange={checkedHandler} id={id} />
                    &nbsp;{title}&nbsp;
                </label>
            </li>
        </>
    );
}
