import { useState } from "react";
import Item from "./Item";
export default function ItemList({ inf, checkedItemHandler, id }) {
    const [isClicked, setIsClicked] = useState(false);
    const click = () => {
        setIsClicked(!isClicked);
    };
    const moreInfo = {
        display: "inline-block",
    };
    const lessInfo = {
        display: "none",
    };
    let index = 0;
    return (
        <dd className="item_dd">
            <ul className="item_list item_list_popular">
                {inf.map((infData, i) => {
                    if (i < 1) {
                    } else if (i < 6) {
                        return (
                            <Item
                                key={infData.name}
                                title={infData.name}
                                checkedItemHandler={checkedItemHandler}
                                id={id}
                            />
                        );
                    }
                })}
            </ul>
            <ul
                className="item_list item_list_all"
                style={isClicked ? moreInfo : lessInfo}
            >
                {inf.map((infData, i) => {
                    index = i;
                    if (i >= 6) {
                        return (
                            <Item
                                key={infData.name}
                                title={infData.name}
                                checkedItemHandler={checkedItemHandler}
                                id={id}
                            />
                        );
                    }
                })}
            </ul>
            {inf.length < 5 ? (
                null
            ) : (
                <div className="spec_opt_view">
                    <button
                        type="button"
                        className="btn_spec_view btn_view_more"
                        style={isClicked ? lessInfo : moreInfo}
                        onClick={click}
                    >
                        <strong>{index}</strong>개
                    </button>
                    <button
                        type="button"
                        className="btn_spec_view btn_view_less"
                        style={isClicked ? moreInfo : lessInfo}
                        onClick={click}
                    >
                        <strong>닫기</strong>
                    </button>
                </div>
            )}
        </dd>
    );
}
