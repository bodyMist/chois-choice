import { useState } from "react";

export default function Item({ inf }) {
  const [isClicked, setIsClicked] = useState(false);
  const click = () => {
    setIsClicked(!isClicked);
  }
  const moreInfo = {
    display: "inline-block",
  };
  const lessInfo = {
    display: "none",
  }
  let index = 0;
    return (
        <dd className="item_dd">
            <ul className="item_list item_list_popular">
                {inf.map((infData, i) => {
                    if (i < 5) {
                        return (
                            <li className="sub_item" key={infData.name}>
                                <label title={infData.name}>
                                    <input
                                        type="checkbox"
                                        title={infData.name}
                                    />
                                    &nbsp;{infData.name}&nbsp;
                                </label>
                            </li>
                        );
                    }
                })}
            </ul>
            <ul className="item_list item_list_all" style={isClicked ? moreInfo : lessInfo}>
                {inf.map((infData, i) => {
                  index = i;
                    if (i >= 5) {
                        return (
                            <li className="sub_item" key={infData.name}>
                                <label title={infData.name}>
                                    <input
                                        type="checkbox"
                                        title={infData.name}
                                    />
                                    &nbsp;{infData.name}&nbsp;
                                </label>
                            </li>
                        );
                    }
                })}
            </ul>
            <div className="spec_opt_view">
                <button type="button" className="btn_spec_view btn_view_more" style={isClicked ? lessInfo : moreInfo} onClick={click}>
                    <strong>{index-4}</strong>개
                </button>
                <button type="button" className="btn_spec_view btn_view_less" style={isClicked ? moreInfo : lessInfo} onClick={click}>
                    <strong>닫기</strong>
                </button>
            </div>
        </dd>
    );
}
