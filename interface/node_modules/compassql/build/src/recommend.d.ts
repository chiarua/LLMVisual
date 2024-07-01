import { QueryConfig } from './config';
import { SpecQueryModelGroup } from './model';
import { Query } from './query/query';
import { Schema } from './schema';
export declare function recommend(q: Query, schema: Schema, config?: QueryConfig): {
    query: Query;
    result: SpecQueryModelGroup;
};
