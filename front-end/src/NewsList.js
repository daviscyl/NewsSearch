import { List } from "antd";
import React, { Component } from "react";
import "./NewsList.css";

class NewsList extends Component {
  render() {
    return (
      <List
        itemLayout="vertical"
        size="large"
        pagination={{
          responsive: true,
          onChange: (page) => {
          },
          pageSize: 10,
        }}
        dataSource={this.props.listData}
        renderItem={(item) => (
          <List.Item key={item.title} extra={<img width={272} alt="logo" src={item.urlToImage} />}>
            <List.Item.Meta
              title={<a href={item.url}>{item.title}</a>}
              description={item.source.name + ", " + item.publishedAt.split("T")[0]}
            />
            {item.content}
          </List.Item>
        )}
      />
    );
  }
}

export default NewsList;
