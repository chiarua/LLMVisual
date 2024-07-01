import { QueryConfig } from './config';
import { SpecQueryModel } from './model';
import { SpecQuery } from './query/spec';
import { Schema } from './schema';
export declare function generate(specQ: SpecQuery, schema: Schema, opt?: QueryConfig): SpecQueryModel[];
